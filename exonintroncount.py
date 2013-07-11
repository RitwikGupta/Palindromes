# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:31:11 2013

@author: Ritwik
"""

def pdromeCount(chrom):
    temp, exonStart, exonEnd, intronStart, intronEnd = [],[],[],[],[]
    dic = {}
    arrKey = []
    exonScore, intronScore = 0,0
    #chrom = input("Chromosome number: ")
    
    with open("./palins/chr" + chrom + "-fa-palin-uniq-txt.tsv") as f:
        next(f)
        for line in f:
        
            tab = line.index("\t")
            key = line[:tab]
            value = line[tab + 1:len(line) - 1]        
            dic[key] = value
            
            arrKey.append(float(key))
            setKey = set(arrKey)
    
    with open("genes_RefSeq_KnownGene.txt") as f:
        next(f)
        for line in f:
            if(line.split("\t")[1] == ("chr" + chrom)):
                exonStartWork = line.split("\t")[8].strip(",").split(",")
                exonStart += map(int, exonStartWork)
                exonEndWork = line.split("\t")[9].strip(",").split(",")
                exonEnd += map(int, exonEndWork)
    
    for i in range(len(exonStart) - 1):
        intronStart.append(exonEnd[i])
        intronEnd.append(exonStart[i + 1])
    
    for i in range(len(exonStart)):
        for key in setKey:
            if key >= exonStart[i] and key <= exonEnd[i]:
                exonScore += 1
    for i in range(len(intronStart)):
        for key in setKey:
            if key >= intronStart[i] and key <= intronEnd[i]:
                intronScore += 1
                    
    print("The exon palindrome count for chromosome " + chrom + " is %s" % exonScore)
    print("The intron palindrome count for chromosome " + chrom + " is %s\n" % intronScore)
    

for i in range(1,9):
    pdromeCount(str(i))
pdromeCount("10")
for i in range(12,23):
    pdromeCount(str(i))