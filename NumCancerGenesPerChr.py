import matplotlib
from pylab import *

x = [1,2,3,4,5,6,7,21,23,8,9,10,11,12,13,14,15,16,17,19,24,18,22,20]
y = [49,30,34,16,17,25,27,5,22,18,28,24,32,25,9,19,12,22,36,28,0,7,14,6]
labels = ["1","2","3","4","5","6","7","21","X","8","9","10","11","12","13","14","15","16","17","19","Y","18","22","20"]     

matplotlib.pyplot.scatter(x,y,color='black')
xlim(xmin=0)
ylim(ymin=0)

grid(True)
xlabel('Chromosomes', fontsize=14)
ylabel('Number of Cancer Genes', fontsize=14)

for i in range(len(x)):
	text(x[i],y[i],labels[i], fontsize=16, color='orange')

matplotlib.pyplot.show()
