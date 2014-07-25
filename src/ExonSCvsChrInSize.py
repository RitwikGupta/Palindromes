import matplotlib
from pylab import *

x = [1,2,3,4,5,6,7,21,23,8,9,10,11,12,13,14,15,16,17,19,24,18,22,20]
y = [30944,25085,19217,14029,16042,17627,14967,5708,12749,13078,15947,13007,
     16210,16877,8138,10416,11287,13275,16314,17595,1501,6287,7246,8378]
labels = ["1","2","3","4","5","6","7","21","X","8","9","10","11","12","13","14","15","16","17","19","Y","18","22","20"]     

matplotlib.pyplot.scatter(x,y,color='black')
xlim(xmin=0)

grid(True)
xlabel('Chromosomes', fontsize=14)
ylabel('Exon SC', fontsize=14)

for i in range(len(x)):
	text(x[i],y[i],labels[i], fontsize=16, color='orange')

matplotlib.pyplot.show()
