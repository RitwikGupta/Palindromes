# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:31:11 2013

@author: Ritwik
"""

temp, exonStart, exonEnd = [],[],[]
dic = {}
arrTwo = []
exonScore = 0

chrom = input("Chr: ")

with open("./palins/chr" + str(chrom[len(chrom)-1]) + "-fa-palin-uniq-txt.tsv") as f:
    next(f)
    for line in f:
    
        tab = line.index("\t")
        key = line[:tab]
        
        value = line[tab + 1:len(line) - 1]
        
        dic[key] = value
        arrTwo.append(key)

with open("genes_RefSeq_KnownGene.txt") as f:
    next(f)
    for line in f:
        if(line.split("\t")[1] == chrom):
            exonStartWork = line.split("\t")[8].strip(",").split(",")
            exonStart += map(int, exonStartWork)
            exonEndWork = line.split("\t")[9].strip(",").split(",")
            exonEnd += map(int, exonEndWork)