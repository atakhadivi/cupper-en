# -*- coding:utf-8 -*-
import urllib2,re
repo="https://github.com/Saferman/password-dictionary/"

def GetHtmlList(url=repo):
    req=urllib2.Request(url)
    f=urllib2.urlopen(req)
    return f.readlines()

    
def CheckUpdate():
    flag = 0
    updateinfo=[]
    for line in GetHtmlList(repo+"blob/master/README.md"):
        if flag==0:
            if re.search('Discription of those dictionaries',line)!=None:
                flag=1
            else:
                continue
        else:
            if line.find('</article>')!=-1:
                break
            m=re.search('<p>DIS_(.*)</p>',line)
            if m==None:
                continue
            else:
                updateinfo.append(m.group(1).split('_'))
    return updateinfo  #a nested list
    

def downfile(dicfile):
    lines=GetHtmlList(repo+"blob/master/"+dicfile)
    f=open(dicfile,'w')
    flag=0
    for line in lines:
        if flag==0:
            if re.search('<div itemprop="text" class="blob-wrapper data type-text">',line)!=None:
                flag=1
            else:
                continue
        else:
            if re.search('</table>',line)!=None:
                break
            m=re.search('blob-code blob-code-inner js-file-line">(.*)</td>',line)
            if m!=None:
                f.write(m.group(1)+'\n')
            else:
                continue
    f.close()
        


    

def download():
    print "[+]Updating password dictionary status from the web..."
    try:
        update=CheckUpdate()
    except:
        print "[-]Unable to get the password dictionary information on the website, please check if the network is smooth."
        return 0
    print "[+]update completed,The password dictionary you can download has:\n"
    for i in xrange(0,len(update)):
        print '    '+str(i+1)+"     "+update[i][0]+" : "+update[i][1]
    while 1:
        down=raw_input("\33[33m> \n Please enter the dictionary number you want to download. ,Enter 99 to exit:\33[0m")
        if down=='99':
            return 0
        if re.search('^\d+$',down)!=None and int(down)<=i+1 and 1<=int(down):
            break
        else:
            print "[-]input error,please enter again"

    print "[+]Downloading file,please wait patiently......"
    try:
        downfile(update[int(down)-1][1])
    except:
        print "[-]error,download failed"
        return 0
    print "[+]success!Download to current directory"+update[int(down)-1][1]+"In the file"
    return 1
    
    























    
    
