"""
"
"
" Author: Ritwik Gupta
"
"
"""
def cancerCount(chrom):
    
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


for i in range(1,23):
    cancerCount(str(i))
