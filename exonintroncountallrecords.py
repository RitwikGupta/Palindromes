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
    dic, dicExonStart = {},{}
    exonScore, intronScore, t0, tf, slExon, slIntron = 0,0,0,0,0,0

    t0 = time.clock()
    with open("./myuniq/chr" + chrom + ".fa.palin.myuniq.txt") as f:
        next(f)
        for line in f:

            tab = line.index("\t")
            tab2 = line.index("\t", tab+1)
            key = line[:tab]
            value = line[tab2 + 1:len(line) - 1]
            
            dic[key] = value            

            arrKey.append(float(key))
    tf = time.clock()
    print("Elapsed time to read chromosome file: " + str(tf-t0))

    with open("hgTables.txt") as f:
        #skip header line
        next(f)

        t0 = time.clock()
        for line in f:

            if(line.split("\t")[1] == ("chr" + chrom)):
                
                #gets the exon start group in that line
                exonStartWork = line.split("\t")[8].strip(",").split(",")
                valueStart = exonStartWork[0]
                exonStart.append(int(valueStart))
                #gets the exon end group in that line
                exonEndWork = line.split("\t")[9].strip(",").split(",")
                valueEnd = exonEndWork[0]
                exonEnd.append(int(valueEnd))
        tf = time.clock()
        print("Elapsed time to add exonStarts and exonEnds to list: " + str(tf-t0))
        
        """for i in range(len(exonStart) - 1):
            if(exonStart[i] == exonStart[i + 1]):
                dicExonStart[str(exonStart[i])] = arrEnds
                dicExonStart[str(exonStart[i])].append(exonEnd[i])"""

        t0 = time.clock()
        for i in range(len(exonStart)):
            fooList = [i for i in range(exonStart[i], exonEnd[i])]
            exonSet.update(set(fooList))
        tf = time.clock()
        print("Elapsed time to add all ranges to set: " + str(tf-t0))

        exonSetList = []
        for item in exonSet:
            exonSetList.append(item)
        exonSetList.sort()
        
        tempCount = 0

        for i in exonSet:
            if i == 9908433:
                tempCount += 1

        print(tempCount)

        ranges = []
        count = 0
        for k, g in groupby(enumerate(exonSetList), lambda (i,x):i-x):
            group = map(itemgetter(1), g)
            if group[0] > 0:
                count += 1
        print(count)
        #print(dicExonStart["9907188"])

        
pdromeCount("21")
