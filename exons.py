# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:31:11 2013

@author: Ritwik
"""
def exonFind(chrom):
    temp, exonStart, exonEnd = [],[],[]
    dic = {}
    arrKey = []
    exonScore = 0
    #chrom = input("Chromosome number: ")
    
    with open("./palins/chr" + chrom + "-fa-palin-uniq-txt.tsv") as f:
        next(f)
        for line in f:
        
            tab = line.index("\t")
            key = line[:tab]
            value = line[tab + 1:len(line) - 1]        
            dic[key] = value
            
            arrKey.append(float(key))
    
    with open("genes_RefSeq_KnownGene.txt") as f:
        next(f)
        for line in f:
            if(line.split("\t")[1] == ("chr" + chrom)):
                exonStartWork = line.split("\t")[8].strip(",").split(",")
                exonStart += map(int, exonStartWork)
                exonEndWork = line.split("\t")[9].strip(",").split(",")
                exonEnd += map(int, exonEndWork)
    for i in range(len(exonStart)):
        for key in arrKey:
            if key >= exonStart[i] and key <= exonEnd[i]:
                exonScore += 1
                    
    print("The exon palindrome count for chromosome " + chrom + " is %s" % exonScore)
    

for i in range(1,9):
    exonFind(str(i))
exonFind("10")
for i in range(12,23):
    exonFind(str(i))