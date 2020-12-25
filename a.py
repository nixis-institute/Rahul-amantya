import numpy as np
def maxx(x,y):
    if(x>=y):
        return x
    else:
        return y

#pair_maxx=np.vectorize(maxx)
a=np.array([5])
b=np.array([6])
#print(pair_maxx(a,b))
print(maxx(a,b))