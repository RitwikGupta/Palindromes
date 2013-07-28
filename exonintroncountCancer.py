"""
"
"
" Author: Ritwik Gupta
"
"
"""

kgidList = []
exonStartWork = []
exonEndWork = []
exonStart = []
exonEnd = []
arrKey = []

refKgidSet = set()
exonCancerSet = set()
kgidSet = set()

geneRefSeq = {}

exonCancerScore = 0
geneTotalCancerExonCount = 0

with open("./myuniq/chr21.fa.palin.myuniq.txt") as f:
        
    #skip header line
    next(f)
    for line in f:

        tab = line.index("\t")
        tab2 = line.index("\t", tab+1)
        key = line[:tab]
        value = line[tab2 + 1:len(line) - 1]    

        arrKey.append(float(key))

with open("kgIdCancerList.txt") as kg:
    for line in kg:
        kgidList.append(line.strip())
        kgidSet.update(set(kgidList))

with open("genes_RefSeq_KnownGene.txt") as ref:
    next(ref)

    for line in ref:
        tempArr = []
        geneRefSeq[line.strip().split("\t")[0]] = tempArr
        tempArr.append(line.split("\t")[8].strip(",").split(","))
        tempArr.append(line.split("\t")[9].strip(",").split(","))

for i in kgidList:
    if i in geneRefSeq:
        geneTotalCancerExonCount += len(geneRefSeq[i][0])
        for k in range(len(geneRefSeq[i][0])):
            fooList = [j for j in range(int(geneRefSeq[i][0][k]), int(geneRefSeq[i][1][k]))]
            exonCancerSet.update(set(fooList))



for key in arrKey:
    if key in exonCancerSet:
        exonCancerScore += 1

print("SC Cancer: %s" % exonCancerScore)
print("Total exons Cancer: %s\n" % geneTotalCancerExonCount)
