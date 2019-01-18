# -*- coding:utf-8 -*-
"""
The rules I currently use: the scoring system
Password length
Does the password have special characters?
Whether the password is all digital,No extra points at the beginning of 0
Whether the password is all lowercase letters or only the uppercase
Passwords starting with 0 are also deducted
If it is not the beginning of the whole number letter, add points
Whether the password is the second half of the first half of the letter
The password is the first half of the letter, the middle special character, the second half of the number

#The whole letter is only the end is a number according to http://www.freebuf.com/news/topnews/62052.html
"""
from lib.common import CountSpecialCharacter

class passScore:
    def __init__(self):
        self.password=''
        self.score=0

def AlphaNumJudge(string):
    '''
       Determine whether a string is composed of the first half of the letter and the second half of the number
    '''
    for i in xrange(0,len(string)):
        if string[0:i].isalpha() and string[i:].isdigit():
            return True
    return False

def AlphaOneSpecialNumJudge(s):
    '''
       Determine whether a string is composed of the first half of the letter plus a special character and the second half of the number
    '''
    for i in xrange(1,len(s)-1):
        if s[0:i].isalpha() and CountSpecialCharacter(s[i])==1 and s[i+1:].isdigit():
            return True
    return False


def giveScore(p):
    score=0
    LengthRule={6:14,7:10,8:10,9:7,10:6,11:5,12:4} #The remaining length is not divided
    try:
        score += LengthRule[len(p)]
    except KeyError:
        score += 0

    if not p.isalnum():
        score = score - 3*CountSpecialCharacter(p)

    if p.isdigit() and p[0]!='0':
        score += 2
    if p.isalpha() and p[1:].islower():
        score +=2
    if p[0]=='0':
        score -= 3
    if not p.isdigit() and p[0].isalpha():
        score += 1
    if AlphaNumJudge(p) or AlphaOneSpecialNumJudge(p):
        score += 2 

    return score

def merge(left,right):  
    result=[]  
    i,j=0,0  
    while i<len(left) and j<len(right):  
        if left[i].score>=right[j].score:  
            result.append(left[i])  
            i+=1  
        else:  
            result.append(right[j])  
            j+=1  
    result+=left[i:]  
    result+=right[j:]  
    return result 

def merge_sort(seq):
    if len(seq)<=1:
        return seq
    else:
        middle = len(seq)/2
        left = merge_sort(seq[:middle])
        right =merge_sort(seq[middle:])
        return merge(left,right)

def sortByScore(passScoreList):
    '''
       Bubbling sorting time is too low efficiency is not recommended
       It is recommended to use merge sorting, etc.,In fact, you don’t have to write your own algorithm.,Python has an algorithm encapsulated in the module
    '''
    """
    for i in xrange(0,len(passScoreList)):
        for j in xrange(i+1,len(passScoreList)):
            if passScoreList[j].score > passScoreList[i].score:
                passScoreList[i],passScoreList[j] = passScoreList[j],passScoreList[i]
        passScoreList[i] = passScoreList[i].password
    return passScoreList
    """
    passScoreList = merge_sort(passScoreList)

    #raw_input()
    for i in xrange(0,len(passScoreList)):
        passScoreList[i] = passScoreList[i].password
    return passScoreList
    

    

def passwordsort(passwordlist,PL=None):
    '''
       Sort by the probability that this password will be used by the user
       Return to the list of completed passwords
    '''
   
    for i in xrange(0,len(passwordlist)):
        p=passScore()
        p.password=passwordlist[i]
        p.score=giveScore(passwordlist[i])
        passwordlist[i]=p
    #This part is very time consuming
    #print "[+]All passwords are scored,Start sorting below"
    return sortByScore(passwordlist)



