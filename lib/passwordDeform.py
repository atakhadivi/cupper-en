# -*- coding: utf-8 -*-
"""
In the actual environment, we found that users may come up with a password.
For some reasons, the password is processed again, such as case change, character replacement, base64 encoding, md5 encryption, etc.
Note: The addition of suffixes is temporarily not a concern for this script.
For the extension of the next version, the mode parameter is reserved here. This parameter has two values.
One is to generate passwords for full coverage, the other is to generate passwords as little as possible, and the appropriate generated passwords (default)
The current processing rules for this script are"""
#Generate passwords as little as possible
"""
Note: The use of these handlers in use, the user may choose serial processing instead of parallel processing
Ensure that there is no conflict between each other.
All functions simply return the processed password, do not contain the unprocessed password and the pre-processing password.
"""
#Each function will explain three things
#1.Suggested conditions for this function to be written by the user before use
#2.This function will handle the passwords that meet the conditions.
#3.What to do
#extra:Explain why this is done

#passL Representative password list
import re
import base64
import hashlib
from lib.common import uppercase,lowercase,number,CountSpecialCharacter
uppers = uppercase()  #Uppercase letter string
lowers = lowercase()  #Lowercase string
numbers =number()     #Numeric string

####Note that the function placed in this file cannot be used to process the result processed by the function.

def CapitalizeTheFirstLetter(passL):
    '''
       Capitalize the first letter of all passwords that are not capitalized at the beginning and all characters are letters (excluding the last digit)
    '''
    r=[]
    for p in passL:
        if p[0] in lowers:
            if p[:-1].isalpha():
                r.append(p.title())#r += p.title()"=This is wrong because the list plus the string is problematic!
        else:
            pass
    #print r
    return r

def charReplace(passL):
    '''
	   No special characters, a-@, o-0, e-3, the first letter is not replaced
       No number, a-4, o-0, e-3, the first letter is not replaced
    '''
    r=[]
    for p in passL:
        if p.isalnum():
            tp=p
            tp=tp[0]+tp[1:].replace('a','@')
            tp=tp[0]+tp[1:].replace('o','0')
            tp=tp[0]+tp[1:].replace('e','3')
            if tp!=p:
                r.append(tp)
        if  re.search('.*([0-9]+).*', p) == None:
            tp=p
            tp=tp[0]+tp[1:].replace('a','4')
            tp=tp[0]+tp[1:].replace('o','0')
            tp=tp[0]+tp[1:].replace('e','3')
            if tp!=p:
                r.append(tp)
    #print r
    return r

def EncodeConvert(passL):
    '''
       Before using, you need to judge whether the test target belongs to the "test target understands safety" scenario.
       Only used to handle passwords without special symbols
       Perform base64, md5 encryption to take the full-length password or intercept the first 8 or the last 8 digits (10 is temporarily not considered)
    '''
    r=[]
    for p in passL:
        if CountSpecialCharacter(p)!=0:
            continue
        try:
            r.append(base64.b64encode(p))
            r.append(base64.b64encode(p)[-8:])
        except:
            pass
        try:
            m = hashlib.md5()
            m.update(p)
            r.append(m.hexdigest())
            r.append(m.hexdigest()[0:8])
        except:
            pass
    print r
    return r



def RandChange(passL):
    '''
       Random transformation, the reason for thinking of this is because of the complexity of the actual environment, the author
       It is impossible to grasp the mental state of each person, so the treatment of this random change is added.
       The function processing does not allow any reasonableness, as long as you like it, maybe someday is right, HH
    '''
    pass

if __name__=='__main__':
    pass
    raw_input()
    