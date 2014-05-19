import numpy as np

a = np.array([1, 2, 3,], dtype=np.float32)



anarray = np.array([ 1.5, -3, 2.])




b = np.linspace(1., 5., 2)


c = np.diag([1, 2, 3, 4, 5, 6]) 
c[0, 0] = 0

d = np.array([ [1, 2], np.array([3, 4]) ])

j = np.array([ [1, 1, 1, 1], np.array([1, 1, 1, 1]), np.array([1, 1, 1, 1]), np.array([1, 1, 1, 1]) ])

j[2, 3] = 2
j[3, 1] = 6



def positive_elements(barray): 

	h = np.delete(barray, [0,1,2,3,4], None)
	
	return h

x = np.arange(10)-5
print x
pos_x = positive_elements(x)
print pos_x

def positive_elements(barray): 

	h = np.delete(barray, [0,1,2,3,4], None)
	
	return h

x = np.arange(10)-5
print x
pos_x = positive_elements(x)
print pos_x