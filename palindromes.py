# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:47:51 2013

@author: Ritwik
"""

for line in open("palindromes.tsv"):
    tab = line.index("\t")
    start = line[:tab]
    sequence = line[tab + 1: len(line) - 1]
    print(sequence)