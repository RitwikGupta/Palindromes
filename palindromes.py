# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

arr = []
counter = 0

with open("palindromesOUT.txt", "wt") as out:
    
    for line in open("palindromesTwo.tsv"):
        
        for i in range(0, len(line) - 4):
            temp = line[i:i + 4]
            reverse = temp[::-1]   #extended slice syntax.
            if temp == reverse:
                arr.append(temp)
                counter += 1
                out.write(temp + "\n")
            
print(arr)
print("\n" + str(counter) + " palindromes in given file")