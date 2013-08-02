# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:31:11 2013

@author: Ritwik Gupta
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""
"                                                 "
"   The function's parameters are:                "
"                                                 "
"       'chrom' AS STRING                         "
"                                                 "
"   chrom is the number of the chromosome.        "
"                                                 "
"   The function calculates and outputs:          "
"                                                 "
"       SC Exon                                   "
"       SC Intron                                 "
"       SL Exon                                   "
"       SL Intron                                 "
"                                                 "
"   in that order.                                "
"                                                 "
"   CoSBBI - DBMI Pitt                            "
"                                                 "
"""""""""""""""""""""""""""""""""""""""""""""""""""
import os

def pdromeCount(chrom):
    
    exonStart, exonEnd, intronStart, intronEnd, arrKey = [],[],[],[],[]
    exonSet, intronSet = set(),set()
    dic = {}
    exonScore, intronScore, slExon, slIntron = 0,0,0,0

    with open("./myuniq/chr" + chrom + ".fa.palin.myuniq.txt") as f:
        
        #skip header line
        next(f)
        for line in f:

            tab = line.index("\t")
            tab2 = line.index("\t", tab+1)
            key = line[:tab]
            value = line[tab2 + 1:len(line) - 1].strip()
            
            dic[key] = value            

            arrKey.append(float(key))

    with open("ScSlOut.txt", "a") as out:
        with open("hgTablesOut.txt") as f:
            
            #skip header line
            next(f)
                  
            for line in f:
                if(line.split("\t")[0] == ("chr" + chrom)):

                    #gets the exon start group in that line
                    exonStartWork = line.split("\t")[1].strip(",").split(",")
                    exonStart += map(int, exonStartWork)
                    #gets the exon end group in that line
                    exonEndWork = line.split("\t")[2].strip(",").split(",")
                    exonEnd += map(int, exonEndWork)
            print(len(exonStart))

        #adds intron Starts and Ends to individual lists
        for i in range(len(exonStart) - 1):

            intronStart.append(exonEnd[i])
            intronEnd.append(exonStart[i + 1])

        #Lookup key in exonSet

        for i in range(len(exonStart)):

            #makes a list of all the positions in an exon
            fooList = [i for i in range(exonStart[i], exonEnd[i] + 1)]
            #appends the list to the exon set
            exonSet.update(set(fooList))

        for i in range(len(intronStart)):

            #makes a list of all the position in an intron
            fooLost = [i for i in range(intronStart[i], intronEnd[i] + 1)]
            #appends the list to the intron set
            intronSet.update(set(fooLost))

        for key in arrKey:

            if key in exonSet:
                exonScore += 1
                slExon += len(dic[str(int(key))])

        #Lookup key in intronSet

        for key in arrKey:

            if key in intronSet:
                intronScore += 1
                slIntron += len(dic[str(int(key))])

        out.write("The exon palindrome count for chromosome " + chrom + " is %s" % exonScore)
        out.write("The intron palindrome count for chromosome " + chrom + " is %s" % intronScore)
        out.write("The score length for exons of chromosome " + chrom + " is %s" % (slExon/8.0))
        out.write("The score length for introns of chromosome " + chrom + " is %s\n" % (slIntron/8.0)) #new line at end

#---------------MAIN---------------
    
for i in range(1,23):
    pdromeCount(str(i))
pdromeCount("X")
pdromeCount("Y")
pdromeCount("21")
