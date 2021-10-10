import numpy as np
from sklearn import linear_model

#X=[3.8, 3.67, 4.02]
#Y=[7.6, 7.3, 8.1]

def func(X, y):

	coef=[]

	X=np.array(X)
	y=np.array(y)
	X=X.reshape(X.shape[0], 1)
	y=y.reshape(y.shape[0], 1)
	
	lr=linear_model.LinearRegression(fit_intercept=False)
	lr.fit(X, y)

	#print(lr.predict(X))
	coef.append(lr.coef_)

	gd=linear_model.SGDRegressor(fit_intercept=False)
	gd.fit(X, y)

	#print(gd.predict(X))
	coef.append(gd.coef_)

	return coef

#print(func(X, Y))