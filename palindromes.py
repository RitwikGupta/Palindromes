# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

dic = {}
arrTwo = []
window = int(input("Window: "))

#initialize array with 'number' + 1 elements of 0
    
for line in open("./palins/chr1-fa-palin-uniq-txt.tsv"):
    
    tab = line.index("\t")
    key = line[:tab]
    
    #line - 1 because there is a /n at the end
    value = line[tab + 1:len(line)]
    
    dic[key] = value
    arrTwo.append(key)
    
print(int(arrTwo[len(arrTwo) - 1]))
number = int(arrTwo[len(arrTwo) - 1]) / window

arr = [0 for i in range(0, int(number + 1))]

for key in dic:
    
    for i in range(int(number + 1)):
        #multiples of window
        if int(key) >= i*window and int(key) < (i+1)*window:
            arr[i] += 1
    
print(arr)