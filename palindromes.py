# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

arr = []

for line in open("palindromes.tsv"):
    tab = line.index("\t")
    start = line[:tab]
    sequence = line[tab + 1: len(line) - 1]
    
    for i in range(0, len(line) - 4):
        temp = line[i:i+4]
        reverse = temp[::-1]
        if temp == reverse:
            arr.append(temp)
            
print(arr)