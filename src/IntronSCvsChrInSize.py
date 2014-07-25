import matplotlib
from pylab import *

x = [1,2,3,4,5,6,7,21,23,8,9,10,11,12,13,14,15,16,17,19,24,18,22,20]
y = [802407,902388,742064,759528,686202,641009,579897,133200,570013,541593,
     437753,479792,473995,478100,387211,327064,287733,259338,245629,156235,
     95170,288356,107173,200445]
labels = ["1","2","3","4","5","6","7","21","X","8","9","10","11","12","13","14","15","16","17","19","Y","18","22","20"]     

matplotlib.pyplot.scatter(x,y,color='black')
xlim(xmin=0)

grid(True)
xlabel('Chromosomes', fontsize=14)
ylabel('Intron SC', fontsize=14)

for i in range(len(x)):
	text(x[i],y[i],labels[i], fontsize=16, color='orange')

matplotlib.pyplot.show()
