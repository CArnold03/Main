import numpy as np
arr1=np.array([[6,7],[2,1]])
arr2=np.array([[1,0],[3,5]])
axis0=np.concatenate((arr1,arr2),axis=0)
axis1=np.concatenate((arr1,arr2),axis=1)
print(axis0)
print()
print(axis1)
