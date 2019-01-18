# -*- coding:utf-8 -*-
import re
from lib.common import addWord

def printpasslistinfo(PL):#passwordlist==PL
    total=0#Total number of passwords
    number=0#Number of pure numeric passwords
    letter=0#Number of pure letter passwords
    specialchar=0#Number of passwords with special characters
    mixNL=0#Number of alphanumeric mixed passwords
    maxlen=0#Maximum password length
    minlen=99#Minimum password length
    mostlen=''#The length of the most frequently generated password
    maxsame='no'#Whether there is a duplicate password
    samecount=0 #Repeat password times
    lendic={}
    lenlist=[]
    mosttime=0

    for i in xrange(0,len(PL)):
        p = PL[i]
        total += 1
        #range3 = 0
        if p.isdigit():
            number += 1
            #range3=1
        if p.isalpha():
            letter += 1
            #range3=1
        if not p.isalnum():
            specialchar +=1
            #range3=1
        else:
            mixNL += 1
        #if range3==0:
            #print p
            #raw_input()
        length=len(p)
        if length > maxlen:
            maxlen = length
        if length < minlen:
            minlen = length
        try:
            lendic[str(length)] += 1
        except KeyError:
            addWord(lendic,str(length),1)#Key character,Value shaping
            lenlist.append(str(length))#character

    samecount = len(PL) - len(set(PL))
    if samecount:
        maxsame='yes'

    print "[+]Information viewed during the debugging process:"
    print lendic
    print lenlist
    #print mosttime
    for l in lenlist:
        if lendic[l] > mosttime:
            mostlen = l
            mosttime = lendic[l]
            continue
        if lendic[l]==mosttime:
            mostlen += ','+str(lendic[l])
            continue
        
    print "\n[+]The password file information you selected is as follows:"
    print "                                 *Total number of passwords(Calculated by row) : "+str(total)
    print "                                 *Number of pure numeric passwords : "+str(number)
    print "                                 *Number of pure uppercase and lowercase letters : "+str(letter)
    print "                                 *Number of alphanumeric mixed passwords : "+str(mixNL)
    print "                                 *Number of passwords containing special characters : "+str(specialchar)
    print "                                 *Maximum password length : "+str(maxlen)
    print "                                 *Minimum password length : "+str(minlen)
    print "                                 *The most frequently occurring password length : "+mostlen+' Coexist:'+str(mosttime)+'Times'
    print "                                 *Duplicate password : "+ maxsame +" frequency : " + str(samecount)

if __name__=="__main__":
    printpasslistinfo(['abcd','1234','123456','1234','we'])
    
        
            
        
    
