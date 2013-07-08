# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

dic = {}

window = int(input("Window: "))

#initialize array with 'number' + 1 elements of 0
    
for line in open("palins/chr1-fa-palin-uniq-txt.tsv"):
    
    tab = line.index("\t")
    key = line[:tab]
    
    #line - 1 because there is a /n at the end
    value = line[tab + 1:len(line) - 1]
    
    dic[key] = value

number = int(int(max(k for k, v in dic.items() if v != 0)) / window)
arr = [0 for i in range(number + 1)]

for key in dic:
    for i in range(number + 1):

        #multiples of window
        if int(key) >= i*window and int(key) < (i+1)*window:
            arr[i] += 1
    
print(arr)