import os
import sys

fn = os.listdir("./geneCheckOut")
suminator = 0

for i in fn:
    with open("./geneCheckOut/" + i) as f:
        next(f)
        for line in f:
            counts = int(line.strip().split("\t")[1])
            suminator += counts

print(suminator)
