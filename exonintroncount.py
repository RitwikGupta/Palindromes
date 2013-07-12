# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:31:11 2013

@author: Ritwik
"""
import time

def pdromeCount(chrom):
    temp, exonStart, exonEnd, intronStart, intronEnd = [],[],[],[],[]
    dic = {}
    arrKey = []
    exonScore, intronScore, t0, tf = 0,0,0,0
    #chrom = input("Chromosome number: ")
    
    with open("./myuniq/chr" + chrom + "-fa-palin-myuniq-txt.tsv") as f:
        next(f)
        for line in f:
        
            tab = line.index("\t")
            key = line[:tab]
            value = line[tab + 1:len(line) - 1]        
            dic[key] = value
            
            arrKey.append(float(key))
    
    with open("genes_RefSeq_KnownGene.txt") as f:
        next(f)
        t0 = time.clock()
        for line in f:
            if(line.split("\t")[1] == ("chr" + chrom)):
                exonStartWork = line.split("\t")[8].strip(",").split(",")
                exonStart += map(int, exonStartWork)
                exonEndWork = line.split("\t")[9].strip(",").split(",")
                exonEnd += map(int, exonEndWork)
        tf = time.clock()
        print("Elapsed time to split and map exons from gene file: " + str(tf-t0))
    
    t0 = time.clock()
    for i in range(len(exonStart) - 1):
        intronStart.append(exonEnd[i])
        intronEnd.append(exonStart[i + 1])
    tf = time.clock()
    print("Elapsed time to calculate and add introns to array: " + str(tf-t0))
        
    """------------The search starts here------------"""
    t0 = time.clock()
    for i in range(len(exonStart)):
        for key in arrKey:
            if key >= exonStart[i] and key <= exonEnd[i]:
                exonScore += 1
                """if exonScore % 10 == 0:
                    #prints the exonScore at intervals of 10
                    print(exonScore)"""
    tf = time.clock()
    print("Elapsed time to search exons: " + str(tf-t0))
    
    t0= time.clock()
    for i in range(len(intronStart)):
        for key in arrKey:
            if key >= intronStart[i] and key <= intronEnd[i]:
                intronScore += 1
    tf = time.clock()
    print("Elapsed time to search introns: " + str(tf-t0))
    """------------The search ends here------------"""
                    
    print("The exon palindrome count for chromosome " + chrom + " is %s" % exonScore)
    print("The intron palindrome count for chromosome " + chrom + " is %s\n" % intronScore)
    
#the function needs the number of chromosome as a string
for i in range(14,19):
    pdromeCount(str(i))