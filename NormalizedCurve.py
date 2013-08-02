import matplotlib
from pylab import *

x = [1,6,5,4,3,2,7,21,23,8,9,10,11,12,13,14,15,16,17,19,24,18,22,20]
y = [0.678498159,0.788562888,0.79601355,0.854725648,0.808739476,0.797794372,
     0.774792311,0.183045083,0.830843867,0.81362082,0.680901961,0.749980375,
     0.746889314,0.880899062,0.774675886,0.675824605,0.668642053,0.669735321,
     0.658639057,0.519028839,0.343594614,1.038731716,0.435906865,0.868652425]
labels = ["1","2","3","4","5","6","7","21","X","8","9","10","11","12","13","14","15","16","17","19","Y","18","22","20"]     

matplotlib.pyplot.scatter(x,y,color='black')
xlim(xmin=0)

grid(True)
xlabel('Chromosomes', fontsize=14)
ylabel('Intron Density (%)', fontsize=14)

for i in range(len(x)):
	text(x[i],y[i],labels[i], fontsize=16, color='orange')

matplotlib.pyplot.show()