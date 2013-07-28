"""
"
" Author: Ritwik Gupta
"
"
"""
import time
import os
import sys

def geneCheck(chrom, filename):

    patLineSplit, patStart, patEnd, hugo = [],[],[],[]
    palinStart, palinEnd = [],[]
    patListSet, palinListSet = set(), set()
    t0, tf, counter = 0,0,0

    if not os.path.exists("./geneCheckOut"):
        os.makedirs("./geneCheckOut")
    
    with open("./geneCheckOut/geneCheckOut_" + filename + ".txt", "a") as out:
        with open("./myuniq/chr" + chrom + ".fa.palin.myuniq.txt", "r") as f:
            
            t0 = time.clock()
            for line in f:
                #gets the exon start group in that line
                palinStart.append(int(line.strip().split("\t")[0]))
                #gets the exon end group in that line
                palinEnd.append(int(line.split("\t")[1].strip(",").split(",")[0]))
            tf = time.clock()
            print("Elapsed time to add all palin lengths to set: " + str(tf-t0))
                
            with open("./Level_2/" + filename) as pat:
                
                for line in pat:
                    patLineSplit = line.strip().split("\t")
                    
                    if patLineSplit[4] == chrom:
                        tempStart = int(patLineSplit[5])
                        tempHugo = patLineSplit[0]
                        tempEnd = int(patLineSplit[6]) + 1
                        patList = [i for i in range(tempStart, tempEnd)]
                        for i in range(len(palinStart)):
                            if(palinStart[i] <= tempStart <= palinEnd[i]):
                                counter += 1
                                hugo.append(tempHugo)

        out.write(str(chrom) + "\t" + str(counter) + "\t")
        for i in hugo:
            out.write(i + ",")
        out.write("\n")
        print("Chr " + chrom + " written")
        out.close()

fn = os.listdir("./Level_2")

controlVar = True

for k in fn:
    if controlVar:
        os.path.exists("./geneCheckOut/geneCheckOut_" + k + ".txt") and os.remove("./geneCheckOut/geneCheckOut_" + k + ".txt")
        controlVar = False
    for i in range(1,23):
        geneCheck(str(i), k)
    geneCheck("X", k)
    geneCheck("Y", k)
