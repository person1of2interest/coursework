#num=[15, 3, 2, 4, 3, 6, 7, 8, 9]

#в условии указано, что массив нумеруется с единицы
#это учитывается в решении
#поэтому результаты нужно интерпретировать соответствующе

def func(m):
	
	a=[0]*len(m)
	b=[0]*len(m)
	check=False
	check2=False
	c=0
	
	for i in range(0,len(m)):
		
		for j in range(0, i):
			if m[j]>m[i]:
				check=True
				a[i]=j+1
			if check:
				break
		
		check=False
		
		for k in range(i, len(m)):
			if m[k]>m[i]:
				check2=True
				b[i]=k+1
			if check2:
				break
		
		check2=False
		
		c+=a[i]*b[i]
	
	return c
	
#print(num)
#print(func(num))