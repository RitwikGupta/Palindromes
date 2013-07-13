# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:31:11 2013

@author: Ritwik
"""
import time

def pdromeCount(chrom):
    temp, exonStart, exonEnd, intronStart, intronEnd = [],[],[],[],[]
    exonSet, intronSet = set(),set()
    arrKey = []
    exonScore, intronScore, t0, tf, sl = 0,0,0,0,0

#==============================================================================
#     """------------Module 1------------"""
#==============================================================================
    t0 = time.clock()
    with open("./myuniq/chr" + chrom + ".fa.palin.myuniq.txt") as f:
        next(f)
        for line in f:

            tab = line.index("\t")
            tab2 = line.index("\t", tab+1)
            key = line[:tab]
            value = line[tab2 + 1:len(line) - 1]

            arrKey.append(float(key))
            sl += len(value)
    tf = time.clock()
    print("Elapsed time to read chromosome file: " + str(tf-t0))
#==============================================================================
#     """------------Module 1------------"""
#==============================================================================

#==============================================================================
#     """------------Module 2------------"""
#==============================================================================
    with open("genes_RefSeq_KnownGene.txt") as f:
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
        print("Elapsed time to split and map exons from gene file: " + str(tf-t0))
#==============================================================================
#         """------------Module 2------------"""
#==============================================================================

#==============================================================================
#     """------------Module 3------------"""
#==============================================================================
    t0 = time.clock()
    #adds the spaces left between the exons as introns
    for i in range(len(exonStart) - 1):

        intronStart.append(exonEnd[i])
        intronEnd.append(exonStart[i + 1])

    tf = time.clock()
    print("Elapsed time to calculate and add introns to array: " + str(tf-t0))
#==============================================================================
#     """------------Module 4------------"""
#==============================================================================

#==============================================================================
#     """------------The search starts here / Module 5------------"""
#==============================================================================
    t0 = time.clock()

    for i in range(len(exonStart)):

        #makes a list of all the positions in an exon
        fooList = [i for i in range(exonStart[i], exonEnd[i] + 1)]
        #appends the list to the exon set
        exonSet.update(set(fooList))

    for key in arrKey:

        if key in exonSet:
            exonScore += 1

    tf = time.clock()
    print("Elapsed time to search exons: " + str(tf-t0))

    t0= time.clock()
    intronStartChunks = [intronStart[x:x+10000] for x in range(0, len(intronStart), 10000)]
    intronEndChunks = [intronEnd[x:x+10000] for x in range(0, len(intronEnd), 10000)]
    for k in range(1, 10000):
        for i in range(len(intronStartChunks[k])):

            #makes a list of the positions in an intron
            fooList = [i for i in range(intronStartChunks[k][i], intronEndChunks[k][i] + 1)]
            #appends the list to the intron set
            intronSet.update(set(fooList))

        for key in arrKey:
            if key in intronSet:
                intronScore += 1
                if intronScore % 10 == 0:
                    print(intronScore)

        tf = time.clock()
    print("Elapsed time to search introns: " + str(tf-t0))
#==============================================================================
#     """------------The search ends here / Module 5------------"""
#==============================================================================

    print("The exon palindrome count for chromosome " + chrom + " is %s" % exonScore)
    print("The intron palindrome count for chromosome " + chrom + " is %s" % intronScore)
    print("The score length for chromosome " + chrom + " is %s\n" % (sl/8.0))

#the function needs the number of chromosome as a string
for i in range(2,23):
    pdromeCount(str(i))
