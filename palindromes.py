# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

dic = {}
countArr = [0,0,0,0,0]

    
for line in open("palindromesTHREE.tsv"):
    
    tab = line.index("\t")
    key = line[:tab]
    value = line[tab + 1:len(line) - 1]
    
    dic[key] = value
        
for key in dic:
    if int(key) >= 0 and int(key) < 10000000:
        countArr[0] += 1
    elif int(key) >= 10000000 and int(key) < 20000000:
        countArr[1] += 1
    elif int(key) >= 20000000 and int(key) < 30000000:
        countArr[2] += 1
    elif int(key) >= 30000000 and int(key) < 40000000:
        countArr[3] += 1
    else:
        countArr[4] += 1
    
print(countArr)