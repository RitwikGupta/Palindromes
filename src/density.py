# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:44:15 2013

@author: Ritwik
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
            value = line[tab2 + 1:len(line) - 1]
            
            dic[key] = value            

            arrKey.append(float(key))
    
    with open("hgTablesOut.txt") as f:
        
        #skip header line
        next(f)
              
        for line in f:
            if(line.split("\t")[1] == ("chr" + chrom)):

                #gets the exon start group in that line
                exonStartWork = line.split("\t")[8].strip(",").split(",")
                exonStart += map(int, exonStartWork)
                #gets the exon end group in that line
                exonEndWork = line.split("\t")[9].strip(",").split(",")
                exonEnd += map(int, exonEndWork)

    #adds intron Starts and Ends to individual lists
    for i in range(len(exonStart) - 1):

        intronStart.append(exonEnd[i])
        intronEnd.append(exonStart[i + 1])

    print("shit")
    #Lookup key in exonSet
    counter = 0
    for i in range(len(exonStart)):

        #makes a list of all the positions in an exon
        fooList = [k for k in range(exonStart[k], exonEnd[k] + 1)]
        #appends the list to the exon set
        exonSet = (set(fooList))

        for key in arrKey:
            if key > exonStart[i] and key in exonSet:
                counter += 1
                if counter % 10 == 0:
                    print(counter)
                break

    print("These many exons contain at least 1 palindrome in chr " + chrom + ": %s" % counter )
    
#---------------MAIN---------------
    
for i in range(1,23):
    pdromeCount(str(i))
pdromeCount("X")
pdromeCount("Y")
pdromeCount("M")
