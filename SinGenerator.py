import numpy as np

sinarray = []

for i in np.arange(0,6.3,0.1):
	sinarray.append([i,np.sin(i)])

print(sinarray)