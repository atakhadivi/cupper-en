# -*- coding: utf-8 -*-

def check(modeList):
    for i in modeList:
        #Add a new scene, also need to be modified here
        if i.isdigit() and i in ['1','2','3']:
            pass
        else:
            return False
    return True

def situationInput(mColor):
    SituationDict={}
    '''
       SituationDict dictionary structure:
       'mode':[a list of characters, including applicable scenarios]
		Other information key-value storage    '''
    while 1:
        print mColor.getInput_Color+"Please select the matching scene below, if not, choose other:"
        print mColor.choice_Color
        #This order here can't be changed casually.
        print "1.Other (default)"
        print "2.The password dictionary is used to guess the password of a user's website account."
        print "3.Test objectives understand security-related knowledge (especially some coding encryption knowledge)"
        numbers = raw_input(mColor.getInput_Color+">Enter the number you want to select (multiple numbers are used, separated):")
        modeList=[]
        if numbers=='':
            modeList.append('1')
        else:
            modeList=numbers.split(',')
            if check(modeList):
                pass
            else:
                print mColor.error_Color+"[-]Input error, please enter a number that can be selected or directly enter!"
                continue

        SituationDict['mode']=modeList

        for mode in modeList:
            if mode=='1':
                pass
            if mode=='2':
                SituationDict['2websiteName'] = raw_input(mColor.getInput_Color+">Please enter the pinyin of the full name of the website, all lowercase, separated by spaces, for example: wang yi you xiang:")
                SituationDict['2domainName'] = raw_input(mColor.getInput_Color+">Please enter the content between the site-level domain name.. (case sensitive), such as baidu:")
                pass
            if mode=='3':
                pass
        break


    return SituationDict
