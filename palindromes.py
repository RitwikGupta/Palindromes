# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

dic = {}

window = int(input("Window: "))
number = int(input("Number: "))

#initialize array with 'number' + 1 elements of 0
arr = [0 for i in range(number + 1)]
    
for line in open("palindromesTHREE.tsv"):
    
    tab = line.index("\t")
    key = line[:tab]
    
    #line - 1 because there is a /n at the end
    value = line[tab + 1:len(line) - 1]
    
    dic[key] = value

for key in dic:
    for i in range(number + 1):
        
        #multiples of window
        if int(key) >= i*window and int(key) < (i+1)*window:
            arr[i] += 1
    
print(arr)