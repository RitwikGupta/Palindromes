# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

dic = {}
countOne = 0; countTwo = 0; countThr = 0; countFou = 0;

with open("palindromesOUT.txt", "wt") as out:
    
    for line in open("palindromesTHREE.tsv"):
        
        tab = line.index("\t")
        key = line[:tab]
        value = line[tab + 1:len(line) - 1]
        
        dic[key] = value
        
for key in dic:
    if int(key[0]) == 1:
        countOne += 1
    elif int(key[0]) == 2:
        countTwo += 1
    elif int(key[0]) == 3:
        countThr += 1
    elif int(key[0]) == 4:
        countFou += 1
        
print("countOne: " + str(countOne), "\ncountTwo: " + str(countTwo))
print("countThr: " + str(countThr), "\ncountFou: " + str(countFou))