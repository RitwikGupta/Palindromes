# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

sc, sl = 0,0
dic = {}
arrTwo = []

chrom = input("Chr: ")
window = int(input("Window: "))

#initialize array with 'number' + 1 elements of 0
with open("./palins/" + chrom + "-fa-palin-uniq-txt.tsv") as f:
    next(f)
    for line in f:
    
        tab = line.index("\t")
        key = line[:tab]
        
        value = line[tab + 1:len(line) - 1]
        
        sl += len(value)
        
        dic[key] = value
        arrTwo.append(key)
    
number = int(arrTwo[len(arrTwo) - 1]) / window

arr = [0 for i in range(0, int(number + 1))]

for key in dic:
    
    for i in range(int(number + 1)):
        #multiples of window
        if int(key) >= i*window and int(key) < (i+1)*window:
            arr[i] += 1
 
print("\nYou have (approx.) %s windows. The values in your windows are: \n" % int(number))
print(arr)

sc = sum(arr)
print("\nScore Count (SC): %s" % sc)
print("Score Length (SL): %s" % (sl/8))