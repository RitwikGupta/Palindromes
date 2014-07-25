# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:18:04 2013

@author: Ritwik
"""

from operator import itemgetter
from itertools import groupby
import time

def pdromeCount(chrom):
    
    temp, exonStart, exonEnd, intronStart, intronEnd = [],[],[],[],[]
    exonSet, intronSet = set(),set()
    arrKey, arrEnds = [],[]
    dic = {}
    exonScore, intronScore, t0, tf, slExon, slIntron = 0,0,0,0,0,0

    t0 = time.clock()
    
    with open("./myuniq/chr" + chrom + ".fa.palin.myuniq.txt") as f:
        
        next(f)
        for line in f:

            tab = line.index("\t")
            key = line[:tab]      

            arrKey.append(float(key))
            
    tf = time.clock()
    print("Elapsed time to read chromosome file: " + str(tf-t0))

    with open("hgTablesDupRemOut.txt", "a") as out:        
        with open("hgTablesDupRem.txt") as f:
            
            #skip header line
            next(f)

            t0 = time.clock()
            for line in f:

                if(line.split("\t")[1] == ("chr" + chrom)):
                    
                    #gets the exon start group in that line
                    exonStartWork = line.split("\t")[8].strip(",").split(",")
                    exonStart += map(int, exonStartWork)
                    
                    #gets the exon end group in that line
                    exonEndWork = line.split("\t")[9].strip(",").split(",")
                    exonEnd += map(int, exonEndWork)
                    
            tf = time.clock()
            print("Elapsed time to add exonStarts and exonEnds to list: " + str(tf-t0))

            #remove duplicates using a set (union)
            t0 = time.clock()
            for i in range(len(exonStart)):
                
                fooList = [i for i in range(exonStart[i], exonEnd[i] + 1)]
                exonSet.update(set(fooList))
                
            tf = time.clock()
            print("Elapsed time to add all ranges to set: " + str(tf-t0))

            #convert exonSet to sorted list
            t0 = time.clock()
            
            exonSetList = []
            for item in exonSet:
                
                exonSetList.append(item)
                
            exonSetList.sort()
            
            tf = time.clock()
            print("Elapsed time to convert set to sorted list: " + str(tf-t0))

            #write exonStart and exonEnd (s, e) ranges to file
            t0 = time.clock()
            
            for k, g in groupby(enumerate(exonSetList), lambda (i,x):i-x):
                
                group = map(itemgetter(1), g)
                out.write(".\tchr" + str(chrom) + "\t\t\t\t\t\t\t" + str(group[0]) + "\t" + str(group[-1]) + "\t\t\n")
                
            tf = time.clock()
            print("Elapsed time to write data to file: " + str(tf-t0))

        out.close()

#---------------MAIN

for i in range(1,23):
    
    pdromeCount(str(i))
    
pdromeCount("X")
pdromeCount("Y")
pdromeCount("M")
