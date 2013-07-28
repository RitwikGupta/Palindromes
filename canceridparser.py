"""
"
"
" Author: Ritwik Gupta
"
"
"""

hugo = []
kgid = []
kgidSet = set()

with open("cancerGeneList.txt") as cgl:
    for line in cgl:
        hugo.append(line.strip())

with open("kgXref.txt") as kg:
    for line in kg:
        for i in hugo:
            if i in line:
                kgid.append(line.strip().split("\t")[0])
kgidSet = set(kgid)
kgid = list(kgidSet)

with open("kgIdCancerList.txt", "w") as out:
    for i in kgid:
        out.write(i + "\n")
