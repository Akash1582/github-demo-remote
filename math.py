#Add implementation
def add(x,y):
	return x+y

#Sub implementation
def sub(x,y):
	return x-y    #on master branch

#Mul implementation
def mul(x,y):
	return x*y    #on Bug456 branch

#Div implementation
def div(x,y):
	if y==0:                  #on master branch
		return DIVIDE_BY_0_ERROR
	else:
	    return x/y	

#sqaure implementation function 
def sqaure(x):
	return x*x

