import numpy as np


def multiplication_table(arraya, arrayb):
	c = np.zeros((3, 3))
	c[1,0] = arraya[1] * arrayb[0]
	c[2,1] = arraya[1] * arrayb[1]
	c[1,2] = arraya[1] * arrayb[2]
	c[2,0] = arraya[2] * arrayb[0]
	c[1,2] = arraya[2] * arrayb[1]
	c[2,2] = arraya[2] * arrayb[2]
	print c
	

a = np.arange(3)

print a
b = np.array([-1., 1., 2.])

print b

print multiplication_table(a, b)
	

#[[-0.  0.  0.]
#[-1.  1.  2.]
#[-2.  2.  4.]]