# -*- coding: utf-8 -*-
from lib.common import getNameList


def Situation2(websiteName,domainName):
    '''
       websiteName  The pinyin of the website name, all lowercase, separated by spaces
       domainName  ..Between strings, case sensitive, such as baidu
    '''
    word_List = getNameList(websiteName)+[domainName]
    #Consider adding a suffix such as 'dmm'
    number_List=[]
    return word_List,number_List




def SituationHandle(SituationDict):
    '''
       Return to the second-level nested list,
       The first list is a list of keywords with the nature of MixedKeywordList
       The second list is InnerNumList (a list of numeric embeddings that the target password may contain)
       Currently supported scenarios:
       1.other
       2.Website user password
       3.Test objectives understand safety
    '''
    words_List=[]
    numbers_List=[]
    for mode in SituationDict['mode']:
        if mode=='1':
            continue
        if mode=='2':
            word_List,number_List = Situation2(SituationDict['2websiteName'],SituationDict['2domainName'])
            words_List += word_List
            numbers_List += number_List
            continue 
        if mode=='3':
            continue
    return [words_List,numbers_List]


    