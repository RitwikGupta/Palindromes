def calcSL(fn):
    A=[]
    #list of palstarts
    B=[]
    #list of palindromes
    length=0
    ans=[0]*25
    fh= open("./myuniq/" + fn + ".fa.palin.myuniq.txt", "r")
    for line in fh:
        elements = line.strip().split()
        start= int(elements[0])
        A.append(start)   
        pal= elements[2]   
        val=len(pal)
        B.append(val)
    for i in A:
        num= int(float(i)/10000000)
        for j in range(len(ans)):
            if(num == j):
                for m in range(len(B)):
                    length += B[m]/8.0
                    print(length)
                ans[j]=length
    print(fn + str(ans))


for k in range(1,23): 
    calcSL("chr" + str(k))
calcSL("chrX")
calcSL("chrY")
calcSL("chrM")
