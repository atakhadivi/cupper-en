# -*- coding:utf-8 -*-
import platform
 
def isWindowsSystem():
    return 'Windows' in platform.system()
 
def isLinuxSystem():
    return 'Linux' in platform.system()

def uppercase():
    r=''
    for s in xrange(65,91):
        r+=chr(s)
    return r

def lowercase():
    r=''
    for s in xrange(97,123):
        r+=chr(s)
    return r
def number():
    r=''
    for s in xrange(48,58):
        r+=chr(s)
    return r

def CountSpecialCharacter(s):
    '''
       Calculate the special characters that appear in a string, return the number
       The special characters here include:@_#$!%^&*.
    '''
    r=0
    r += s.count('@')
    r += s.count('_')
    r += s.count('#')
    r += s.count('$')
    r += s.count('!')
    r += s.count('%')
    r += s.count('^')
    r += s.count('&')
    r += s.count('*')
    r += s.count('.')
    return r

    
def FilterList(alist):#Filter list of the same elements
    return list(set(alist))

def addWord(dic,key,value):
    #Existence Key:Value to dictionary dic, create a new dictionary key if it does not exist
    dic.setdefault(key,value)

def getNameList(name):
    '''
     Get the pliers from the full name, the name must obey the following format
     It is best to handle the company name, the full name of the website, such name      
     Pinyin of the full name, all lowercase, separated by spaces
    '''
    r=[]
    nameSplited = name.split()
    func = lambda x:[x.lower(),x[0],x[0].upper()]#3, so the loop below is also 3
    for i in xrange(0,len(nameSplited)):
        nameSplited[i]=func(nameSplited[i])
    for j in xrange(0,3):
        s=''
        for i in xrange(0,len(nameSplited)):
            s += nameSplited[i][j]
        r.append(s)
    return r

def SessionCommandInput(mColor):
    '''
       This script writes the input of the persistent command mode.
       Mainly used for session file management
    '''




if __name__=='__main__':
    d={}
    addWord(d,'1',1)
    print d['1']+1
    
