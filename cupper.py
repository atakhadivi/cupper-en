# -*- coding: utf-8 -*-
#!/usr/bin/env python
#  [tool]
#  cupper 2.0
#  Password generation tool
#
#  [Author]
#  Name:Ata Khadivi, Saferman
#  
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.
import sys
import re
import os
import argparse
from logo.logo import logo
from lib.createpassword import PasswordGenerator
from lib.PDHandle.handlefile import HandleFile
from lib.download import download
from lib.common import SessionCommandInput
from userinput.informationInput import informationInput
from structure.structure import *
from session.interactiveSession import *
from stdout.Windows_stdout import UnicodeStreamFilter


##Define the required structure data:
mColor = meaningColor()


def tag():
    print "\n[+]Thanks for using"
    print ""
    exit()


def checkYourPassword():
    if raw_input(">Do you want to check your password in the password file?y|Y, Not checked by default:").lower()=='y':
        passwordlist=raw_input(">Please enter your password,Multiple passwords to,Separate:").split(',')
        print "[+]Genuine socialpass.dic Find if there is a password you entered......"
        filelist=open('socialpass.dic','r').readlines()
        flag=0#Whether the logo has any password found
        for inputpassword in passwordlist:
            for filepassword in filelist:
                if filepassword.strip('\n')==inputpassword:
                    print "[+]socialpass.dic include password : "+inputpassword
                    flag=1
        if flag==0:
            print "[-]no result"

def ClearNull(PI):
    for attri in PI.__dict__.keys():
        if isinstance(PI.__dict__[attri], list):
            PI.__dict__[attri] = filter(lambda x:x!='', PI.__dict__[attri])
    return PI


def print_version():
    logo()
    print "\r\n	"+mColor.title_Color+"[ cupper.py ]  v2.0"+mColor.normal_Color+"\r\n"
    print "	* Author:Ata Khadivi, Saferman"
    print "	* Download link:https://github.com/atakhadivi/cupper/\r\n"
    print "     * For more explanation or any doubt about this tool, please check README or github wiki\r\n"
    exit()


def ManageSession():
    print "[+]Welcome session management ,session A file is a file that holds information entered by the user during the interactive password generation process. The purpose is to facilitate the user to load the file directly without having to repeatedly input the same information."
    print "[+]Listing existing ones session file"
    sessionList = CheckSession(mColor)
    if not sessionList:
        exit()
    else:
        SessionCommandInput(sessionList,mColor)


def interactive():
    sessionList = CheckSession(mColor)
    if not sessionList:
        PI = False
    else:
        sessionname = raw_input(mColor.getInput_Color+">Do you want to load the session file as your interactive input information? If you want, please enter the file name listed above, otherwise skip:")
        if sessionname in sessionList:
            PI = LoadSession(sessionname,mColor)

    if not PI:
        PI = PersonalInformation()
        PI = informationInput(PI,mColor)
        PI = ClearNull(PI)  #Set all [''] to []
        while 1:
            saveYN = raw_input(mColor.getInput_Color + ">Do you want to save the information you entered as a session file? It is convenient to load this file directly next time without re-entering (y|Y|n|N, not saved by default):").lower()
            if saveYN == 'y':
                if SaveSession(PI,mColor):
                    print mColor.normal_Color + "[+]The entered information is saved into the session file successfully.!"
                else:
                    print mColor.normal_Color + "[-]The input information failed to save the session file"
                break
            if saveYN =='n' or saveYN =='':
                break
            print mColor.error_Color + "[-]Please enter y, Y, n, N or directly enter"

    pg=PasswordGenerator(PI)
    print mColor.normal_Color + "[+]Generating a dictionary file, please be patient......"
    passwordslist=pg.generator()

    print "[+]The build is successful, the program will write the password to the current directory socialpass.dic"
    if os.path.exists("socialpass.dic")==True:
        if raw_input("[-]Warning, the current directory has socialpass.dic, do you want to overwrite? n|N, default override:").lower()=='n':
            exit()
    f=open("socialpass.dic",'w')
    for word in passwordslist:
        f.write(word+'\n')
    f.close()
    print "[+]Write successfully!!socialpass.dic is the last password file"


    checkYourPassword()
    
    

def main():
    reload(sys)
    sys.setdefaultencoding("utf8")
    if sys.stdout.encoding == 'cp936':
        sys.stdout = UnicodeStreamFilter(sys.stdout)

    parser = argparse.ArgumentParser(description="* For more explanation or any doubt about this tool, please check the README or github wiki")
    parser.add_argument('-f','--file',type=str,default=None,help="Various processing of password files",dest='file')
    parser.add_argument('-i','--interactive',help="Interactively generate a password dictionary",action="store_true")
    parser.add_argument('-s','--session',help="Manage session files that save input information",action="store_true")
    parser.add_argument('-d','--download',help="Download the password dictionary maintained by the author",action="store_true")
    parser.add_argument('-v','--version',help="View Logo and Display Tool versions",action="store_true")

    args = parser.parse_args()
    if args.version:
        print_version()
        tag()
    if args.download:
        download()
        tag()
    if args.session:
        ManageSession()
        tag()
    if args.interactive:
        interactive()
        tag()
    if args.file!=None:
        HandleFile(args)
        tag()
        



if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\n[-]It's implite to interrupt me!:("










