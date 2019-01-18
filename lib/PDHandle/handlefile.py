# -*- coding:utf-8 -*-
import os
import re
from lib.PDHandle.passwordinfo import printpasslistinfo
from lib.PDHandle.passwordsort import passwordsort

def ReadStripFile(filenameext):
    lineslist=open(filenameext,'r').readlines()
    for i in xrange(0,len(lineslist)):
        lineslist[i]=lineslist[i].strip()
    return lineslist


def WriteToFile(filenameext,alist):
    f=open(filenameext,'w')
    for a in alist:
        f.write(a+'\n')
    f.close()


def AddSome(l=[],he='h',cover='c',s=''):#He can only be h or e,Cover is c or a,Back to list
    if cover=='c':
        if he=='h':
            for i in xrange(0,len(l)):
                l[i] = s+l[i]
        else:
            for i in xrange(0,len(l)):
                l[i] = l[i]+s
    else:
        if he=='h':
            for i in xrange(0,len(l)):
                l.append(s+l[i])
        else:
            for i in xrange(0,len(l)):
                l.append(l[i]+s)
    return l
            
def Filter(l=[],choice='s',length='6'):
    if choice=='l':
        return [p for p in l if len(p)<=int(length)]
    else:#choice=='s'
        return [p for p in l if len(p)>=int(length)]
            
        

def HandleFile(args):#For args.File file processing
    passfile=args.file
    while 1:
        if not os.path.exists(passfile):
            print "[-]file doesn't exist!"
            break
        
        print "\r\n[+]Your processing object is: "+passfile+" ,The current version supports the processing.:"
        print "1------Check password file and remove redundant duplicates"
        print "2------Add custom content to the beginning or end of each line of password"
        print "3------Filter passwords in the password file that are smaller or larger than the number of digits you specify"
        print "4------Case conversion"
        print "5------Add a password for another dictionary file to the dictionary file"
        print "6------Get information about the contents of the password file(Total number of passwords,Number of pure digital passwords, etc.)"
        print "7------Sort passwords in the password dictionary according to certain rules to improve the efficiency of cracking"
        print "99-----drop out"
        handle=raw_input("\33[33m> Please enter the action you want to take.:\33[0m")

        if handle not in ['1','2','3','4','5','6','7','99']:
            print "[-]input error!!"
            raw_input(">Press any key is to input again:")
            continue

        if handle=='99':
            break
        
        passwordlist=ReadStripFile(passfile)
        
        if handle=='1':
            print "[+]Deleting the same entry as the original password file,Please wait.........."
            passwordlist=list(set(passwordlist))
            WriteToFile(passfile,passwordlist)
            print "[+]Remove duplicates(Keep only one)success,Password file or original file"
            break

        if handle=="2":
            while 1:
                he=raw_input("\33[33m> You want to add a custom character at the beginning or end of each line of password?Starting with h|H,End of e|E:\33[0m").lower()
                if he!="h" and he!="e":
                    print "[-]Please enter h|H or e|E"
                    continue
                else:
                    break
            string=raw_input("\33[33m> Please enter the characters you want to add:\33[0m")
            while 1:
                cover=raw_input("\33[33m> Do you want to overwrite the old password with the password with the added characters or add it to the old password??c|C coverage,a|A add:\33[0m").lower()
                if cover!='c' and cover!='a':
                    print "[-]Please enter c|C or a|A"
                    continue
                else:
                    break
            print "[+]Processing,Please wait......"
            passwordlist=AddSome(passwordlist,he,cover,string)
            WriteToFile(passfile,passwordlist)
            print "[+]Added successfully!"
            break

        if handle=="3":
            while 1:
                filterchoice=raw_input(">You want to filter passwords larger than a certain length(l|L), or a password that is less than a certain length(s|S):").lower()
                if filterchoice!='l' and filterchoice != 's':
                    print "[-]Please enter l|L or s|S"
                    continue
                else:
                    break
            while 1:
                filterlength=raw_input(">(The value entered does not contain):")
                if re.search('^\d+$',filterlength)==None:
                    print "[-]Please enter the number"
                    continue
                else:
                    break
            print "[+]Filtering,Please wait......"
            passwordlist=Filter(passwordlist,filterchoice,filterlength)
            WriteToFile(passfile,passwordlist)
            print "[+]Filter completed"
            break

        if handle=='4':
            while 1:
                print "[-]The number you choose is not one of 1, 2, 3, please re-select"
                print "1-------Convert all letters in all passwords to uppercase"
                print "2-------Convert all letters in all passwords to lowercase"
                print "3-------Convert all passwords first to uppercase(If it is not the letter will not be affected)"
                mo=raw_input("\33[33m> Please select one,Enter the number:\33[0m")
                if mo not in ['1','2','3']:
                    print "[-]You can only enter one of 1, 2, 3"
                    continue
                else:
                    break
            print "[+]Processing case,Please wait.........."
            if mo=="1":
                passwordlist=[p.upper() for p in passwordlist]
            if mo=="2":
                passwordlist=[p.lower() for p in passwordlist]
            if mo=="3":
                passwordlist=[p.title() for p in passwordlist]
            WriteToFile(passfile,passwordlist)
            print "[+]Case processing completed"
            break

        if handle=='5':
            while 1:
                anotherfile=raw_input(">Please enter another password file absolute path(File name suffix):")
                try:
                    anotherPL=ReadStripFile(anotherfile)
                except IOError:
                    print "\n[-]The file you entered does not exist!!"
                    continue
                except:
                    print "\n[-]Error,The file you selected cannot be opened normally.!"
                    continue
                else:
                    break
            print '[+]The file you are about to choose('+anotherfile+')Add to processing file('+passfile+')Behind'
            WriteToFile(passfile,passwordlist+anotherPL)
            print '[+]Added successfully!'
            break
        if handle=='6':
            print "[+]Getting file information about password,Please wait........"
            printpasslistinfo(passwordlist)
            print "[+]Get information done"
            break
            
        if handle=='7':
            print "[+]Sorting passwords in password files"
            passwordlist = passwordsort(passwordlist)
            WriteToFile(passfile,passwordlist)
            print "[+]Sorted out"
            break


























            
            
    
