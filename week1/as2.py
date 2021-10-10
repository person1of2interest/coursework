import numpy as np
import math

#num=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def func(m):
	
	i=0
	j=0
	sum1=0
	sum2=0

	while i<m.shape[0]:
		while j<m.shape[1]:
			sum1+=m[i][j]
			i+=1
			j+=1
	
	i=0
	j-=1
	
	while i<m.shape[0]:
		while j>=0:
			sum2+=m[i][j]
			i+=1
			j-=1
	
	return abs(sum2-sum1)
	
#print(func(num))
