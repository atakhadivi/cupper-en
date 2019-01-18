# -*- coding: utf-8 -*-
import time
import os
import pickle

def CheckSession(mColor,path=os.path.abspath("session")):
    sessionList = []
    for item in os.listdir(path):
        if os.path.isdir(path+item) or item[-2:]=='py' or item[-3:]=='pyc':
            continue
        else:
            sessionList.append(item)
            print mColor.normal_Color + "[+]Found a session file : "+item
    if not sessionList:
        print mColor.normal_Color + "[-]No session file"
    return sessionList


def DeleteSession(sessionname,mColor,path=os.path.abspath("session")):
    try:
        os.remove(path+os.sep+sessionname)
    except WindowsError or OSError:
        print mColor.error_Color + "[-]No such session file"
        return 0
    else:
        print "[+]Successfully deleted"+sessionname+"file"
        return 1


def LoadSession(sessionname,mColor,path=os.path.abspath("session")):
    if os.path.exists(path+os.sep+sessionname):
        sf = open(path+os.sep+sessionname,'rb')
        PI = pickle.load(sf)
        print "[+]Successfully loaded"+sessionname+"Interactive content"
        sf.close()
        return PI
    else:
        print mColor.error_Color + "[-]No"+sessionname+"file"
        return False

def ShowAllSession(mColor,path=os.path.abspath("session")):
    sessionList = CheckSession(mColor,path)
    for sessionname in sessionList:
        PI = LoadSession(sessionname,mColor,path)
        if PI:
            print mColor.normal_Color + "[+]"+sessionname+"Content is as follows:"
            for attri in PI.__dict__.keys():
                print mColor.normal_Color +attri+" : ",
                print PI.__dict__[attri]
        else:
            pass

def ShowSession(sessionname,mColor,path=os.path.abspath("session")):
    PI = LoadSession(sessionname,mColor,path)
    if PI:
        print mColor.normal_Color + "[+]"+sessionname+"Content is as follows:"
        for attri in PI.__dict__.keys():
            print mColor.normal_Color +attri+" : ",
            print PI.__dict__[attri]
    else:
        pass

def SaveSession(PI,mColor,path=os.path.abspath("session")):
    sessionname = raw_input(mColor.getInput_Color+">Please enter the name of the sessionfile (without the suffix, it is recommended to name the target object and date):")
    if os.path.exists(path+os.sep+sessionname):
        print mColor.warn_Color+"[!]caveat:"+sessionname+"already exists"
        if raw_input(mColor.getInput_Color+">Do you want to overwrite this sessionfile??y|Y,The rest does not cover:").lower()=='y':
          pass
        else:
            if raw_input(mColor.getInput_Color+">Do you want to re-enter the sessionfile name??n|N,The rest is:").lower()=='n':
                return 0  
            else:
                if SaveSession(PI,mColor,paths)==1:
                    return 1
                else:
                    return 0
    sf = open(path+os.sep+sessionname,"wb")
    pickle.dump(PI,sf)
    sf.close()
    return 1


def SessionCommandInput(sessionList,mColor):
    '''
       This script writes the input of the persistent command mode.
       Mainly used for session file management
    '''
    print "[+]Please enter help to view help information"
    while 1:
        c = raw_input(mColor.getInput_Color + "ManageSession>").lower().strip()
        cL = c.split()#''.split()The result is[]unless''.split(',')for['']
        if cL == []:
            continue
        if cL[0] == "help":
            if len(cL)!=1:
                print  mColor.error_Color + "[-]Please do not enter extra characters!"
                continue
            else:
                print mColor.choice_Color
                preSpace = 10
                middleSpace = 4
                print " "*preSpace+"show sessionname"+" "*middleSpace + "View the contents of the session file"
                print " "*preSpace+"delete sessionname"+" "*middleSpace + "View the contents of the session file"
                print " "*preSpace+"list sessionname"+" "*middleSpace + "List all session files"
                print " "*preSpace+"help"+" "*middleSpace + "View supported commands"
                print " "*preSpace+"exit"+" "*middleSpace + "drop out"
                continue
        if cL[0] == "show":
            ShowSession(cL[1],mColor)
            continue
        if cL[0] == "delete":
            DeleteSession(cL[1],mColor)
            continue
        if cL[0] == 'list':
            if len(cL)!=1:
                print  mColor.error_Color + "[-]Please do not enter extra characters!"
                continue
            else:
                CheckSession(mColor)
                continue
        if cL[0] == "exit":
            if len(cL)!=1:
                print  mColor.error_Color + "[-]Please do not enter extra characters!"
                continue
            else:
                break
        print mColor.error_Color + "[-]The command format is entered incorrectly! Please follow the help display requirements."