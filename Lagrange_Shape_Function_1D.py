'''
@author: Hossain
'''

import numpy as np

def LagrangeShapeFun1D(myNum):
    m = len(myNum)
    Lf = np.ones((m,m),dtype=int)
    print(m)
    for i in range(1,m+1):
        for j in range(1,m+1):
            if i!=j:
                n1 = np.subtract(myNum,myNum[j-1])
                n2 = myNum[i-1]-myNum[j-1]
                n3 = np.divide(n1,n2)
                Lf[i-1,:]= np.multiply(Lf[i-1,:],n3)
            j +=1
        i +=1
    return Lf

#this part is for testing
#ap = range(1,5) 
    
#print(LagrangeShapeFun1D(ap))

            