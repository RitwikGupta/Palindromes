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
    exonScore, intronScore, t0, tf, sl = 0,0,0,0,0
    
    with open("./myuniq/chr" + chrom + ".fa.palin.myuniq.txt") as f:
        next(f)
        for line in f:
        
            tab = line.index("\t")
            tab2 = line.index("\t", tab+1)
            key = line[:tab]
            value = line[tab2 + 1:len(line) - 1]        
            dic[key] = value
            
            arrKey.append(float(key))
            sl += len(value)            
            
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
    print("The intron palindrome count for chromosome " + chrom + " is %s" % intronScore)
    print("The score length for chromosome " + chrom + " is %s\n" % (sl/8))
    
#the function needs the number of chromosome as a string
for i in range(2,23):
    pdromeCount(str(i))