import matplotlib
from pylab import *

x = [1,2,3,4,5,6,7,21,23,8,9,10,11,12,13,14,15,16,17,19,24,18,22,20]
y = [1691160.875,1917780.000,
1576285.375,
1633844.625,
1463133.125,
1365146.375,
1232994.125,
284215.125,
1216056.500,
1148941.875,
922858.750,
1012522.375,
999725.500,
1014530.375,
831611.000,
692932.375,
604149.875,
543793.000,
514247.250,
327120.625,
204004.375,
614191.500,
223640.125,
418081.500
]

matplotlib.pyplot.scatter(x,y)
xlim([0,25])
xlabel('Chromosomes', fontsize=18)
ylabel('Intron SL', fontsize=16)
xticks(range(len(y)), x, size='small')
(m,b) = polyfit(x,y,1)
print(b)
print(m)

yp = polyval([m,b],x)

plot(x,yp)
grid(True)
title("Intron SL vs. Chromosome\n In order of size")
matplotlib.pyplot.show()


