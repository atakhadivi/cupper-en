# -*- coding:utf-8 -*-
import re

def AnalyzeGetNumbers(oldpasslist):#Extract the key figures that appear from the old password list and return a list of key numbers
    r = []
    renum=re.compile('\d+')
    for oldpass in oldpasslist:
        r += renum.findall(oldpass)
    return r
        
