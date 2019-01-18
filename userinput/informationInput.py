# -*- coding: utf-8 -*-
from userinput.situationInput import situationInput
from userinput.informationCheck import *
from structure.structure import meaningColor

def inputClear(string):
    return string.strip()  #Will remove the spaces on both sides\r\n

def check_raw_input(prompt_string,mColor,check_func=None,error_message="wrong format",):
    while 1:
        content = raw_input(mColor.getInput_Color + prompt_string)
        content = inputClear(content)
        if check_func==None:
            return content
        if check_func(content):
            return content
        else:
            print mColor.error_Color + "[-]" + error_message
            continue

def explain(explain_string,mColor=None):
    mColor = mColor if mColor else meaningColor()
    print mColor.explain_Color + "[*]" + explain_string + "!"

def informationInput(PI,mColor):
    print mColor.normal_Color + "\r\n[+] Fill in the information below to generate a dictionary that only allows characters on a printable American keyboard:"
    print "[+] If you don't know or don't want to fill out, just enter it once.\r\n"
    
    explain("All names include the current name of the target, the real name used in the past (written in pinyin format, case insensitive, separated by spaces. If there are multiple names; separate)")
    PI.fullnameList += check_raw_input(">The full name of the target:", mColor).lower().split(';')
    
    explain("Nickname is sensitive here. If there is a Chinese nickname, please decide whether to provide the English name or pinyin of the nickname according to the situation. Usually there is a comparison." + \
        "Direct and reasonable English translation, it is recommended to provide a lowercase English name. If the nickname contains special characters that cannot be entered, you can ignore this nickname (case insensitive, separate spaces. If there are multiple nicknames; separate)")
    PI.nicknameList += check_raw_input(">Nickname in life (nickname):", \
        mColor).split(';')

    PI.nicknameList += check_raw_input(">Nicknames of goals on major social software (no recommendations that are not specifically included in the password are not filled in, multiple nicknames are separated;:", \
        mColor).split(';')

    PI.qq += check_raw_input(">Target qq number (you can also enter the qq number of the target lover but only allow you to enter one here):", \
        mColor,qqCheck,"Qq must be all numbers")

    explain("Enter a name for a lover, each word separated by a space, where the case is not sensitive")
    PI.lovernameList += check_raw_input(">Please enter the name of the target lover's pinyin:", \
        mColor).lower().split(';')

    explain("Allow multiple nicknames to be entered; separated, words in nicknames separated by spaces, case sensitive")
    PI.nicknameList += check_raw_input(">Please enter the nickname of the target lover:",mColor).split(";")

    PI.dateList += check_raw_input(">Please enter the target birthday, request a total of 8 digits, such as 19980405:", \
        mColor,dateCheck,"Please enter your birthday in the sample format").split(";")

    explain("The anniversaries include the wedding anniversary of the target and the lover, the birthday of the target lover, and the birthday of the most important person around the target (not particularly important, it is recommended not to consider this)")
    PI.dateList += check_raw_input(">Please enter other important commemorative dates related to the target (multiple; separated by a total of 8 digits, such as 19980405):", \
        mColor,dateStringCheck,"Please enter the correct date in the sample format")

    explain("Here is actually the mobile phone number that you want to enter the target, but in reality, your target may use a mobile phone number of his family." + \
        "If you have this possibility, you can fill in multiple phone numbers here, but it is strongly recommended that you choose the most likely one from multiple phone numbers.")
    PI.phoneList += check_raw_input(">Target mobile number (fill in multiple mobile numbers to separate; separate):", \
        mColor,phoneStringCheck,"Enter the phone number must be all digits").split(";")

    PI.oldpasswdList += check_raw_input(">The old password you used to know the target (multiple separated by ;):", \
        mColor).split(';')

    explain("This institution can be large-scale and small-scale, such as the school league committee and the academic office, then you should enter tuan wei or jiao wu chu." +\
        "You can enter the name of this school. There are companies, etc. For each name you enter, you must have the first letter of each word to form a combination." + \
        "Abbreviated condition")
    PI.organizationList += check_raw_input(">The full name of the name of the institution in which the target is located (case insensitive, English or Chinese pinyin, multiple; separated):", \
        mColor).lower().split(';')

    #Keywords and key digital extraction
    explain("This section requires you to give the keywords and key figures that the target may use in the password (the keywords and key figures here are not weak passwords)" + \
        "In order to avoid you do not know where to start, here will gradually guide you to extract keywords and key figures from multiple aspects of the target." + \
        "The case is not sensitive, each keyword is separated; separated by keywords within each keyword. Please do not have duplicate content")
    pet_wordsList = check_raw_input(">Keywords related to the target pet or favorite pets, these keywords can be the English name of the pet, the full name of the pet Chinese name (no pets or pets you like, please skip):", \
        mColor).lower().split(';')

    pet_numbersList = check_raw_input(">The key figures associated with the target pet or the pet you like may be the pet's age, birthday, and date of death:", \
        mColor,numberStringCheck,"Only allow numbers to be entered").lower().split(';')

    star_wordsList = check_raw_input(">The keywords related to the favorite stars can come from the names of the stars, English names, etc., and can also be inferred from the relevant information of the favorite stars of the target, such as the things that the stars like, the release albums of the stars, etc.:", \
        mColor).lower().split(';')

    star_numbersList = check_raw_input(">Like the key figures related to the stars, these numbers are usually found online.:", \
        mColor,numberStringCheck,"Only allow numbers to be entered").lower().split(';')

    explain("The specialty here consists of two parts, one is the target hobby, and the other is the regular habit of the target.")
    skill_wordsList = check_raw_input(">Keywords related to target characteristics:", \
        mColor).lower().split(';')

    skill_numbersList = check_raw_input(">Key figures related to target strengths:", \
        mColor,numberStringCheck,"Only allow numbers to be entered").lower().split(';')


    food_wordsList = check_raw_input(">Target favorite food related keywords, usually things Chinese or English or distinguished names:", \
        mColor).lower().split(';')

    food_numbersList = check_raw_input(">Key figures related to your favorite food (usually not here):", \
        mColor,numberStringCheck,"Only allow numbers to be entered").lower().split(';')

    location_wordsList = check_raw_input(">Keywords related to the target home address or office address:", \
        mColor).lower().split(';')

    location_numbersList = check_raw_input(">Key figures related to the target home address or office address:", \
        mColor,numberStringCheck,"Only allow numbers to be entered").lower().split(';')

    explain("Please do not repeat the content filled in. If there is no information that may be included in the password, please do not fill in.")
    relative_wordsList = check_raw_input(">Keywords related to loved ones with deep or important goals:", \
        mColor).lower().split(';')

    relative_numbersList = check_raw_input(">Key figures related to loved ones with deep or important interests:", \
        mColor,numberStringCheck,"Only allow numbers to be entered").lower().split(';')

    explain("The totem property here can be understood as the high probability that the target will be used or has already shown that it is often used or related to the target and meaningful use." +\
        "Keywords and key figures that will be in the password")
    other_wordsList = check_raw_input(">Other keywords that you need to add totem:", \
        mColor).lower().split(';')

    other_numbersList = check_raw_input(">Other key figures with totem properties that you need to add:", \
        mColor,numberStringCheck,"Only allow numbers to be entered").lower().split(';')

    ##Do you choose to add a built-in weak password?
    weakpasswd = check_raw_input(mColor.getInput_Color+">You want to add the built-in weak password in front of the last password dictionary.?y|Y,Default is not added:", \
        mColor).lower()
    if weakpasswd=='y':
        print mColor.normal_Color+"[+]You have chosen to add a built-in weak password."
        weakpasswd=1
    else:
        print mColor.normal_Color+"[-]You have no choice to add a built-in weak password"
        weakpasswd=0

    ##############Increase scene input, get more information according to different scenes and save it to situation in dictionary form
    #This dictionary has at least one 'mode'key whose value refers to the scene from which the dictionary comes from.
    PI.situation=situationInput(mColor)
    ############

    PI.keywordsList = pet_wordsList+star_wordsList+skill_wordsList+food_wordsList+location_wordsList+relative_wordsList+other_wordsList
    PI.keynumbersList = pet_numbersList+star_numbersList+skill_numbersList+food_numbersList+location_numbersList+relative_numbersList+other_numbersList
    return PI






