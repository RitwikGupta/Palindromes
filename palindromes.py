# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

dic = {}

window = int(input("Window: "))
number = int(input("Number: "))
arr = [0 for i in range(number + 1)]
    
for line in open("palindromesTHREE.tsv"):
    
    tab = line.index("\t")
    key = line[:tab]
    value = line[tab + 1:len(line) - 1]
    
    dic[key] = value

for key in dic:
    for i in range(number + 1):
        if int(key) >= i*window and int(key) < (i+1)*window:
            arr[i] += 1
    
print(arr)