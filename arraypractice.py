import numpy as np
my_data=np.genfromtxt('StudentExercise.csv', delimiter=',', skip_header=1)
'''print(my_data)
print(my_data[:,0])
print(my_data[0,:])
print(my_data[0:5,0:2])
print(my_data[0:5,0:1])'''
print(my_data[4,3])
