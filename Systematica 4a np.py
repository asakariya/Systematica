import numpy as np

n = 1000000
radius = np.random.randint(1,100)

"""
Creating the points that lie on the circumference of a circle.
Assuming the circle to be centered at (0,0)	
"""
def Circle(r,n):

	cumsum = np.cumsum(np.ones((n,1)))-1
	x = np.cos(cumsum*2*np.pi/n)*r
	y = np.sin(cumsum*2*np.pi/n)*r

	return x, y

#Creating a random circle with center (0,0)
x, y = Circle(radius,n)

#length of an equilateral triangle inscribed in a circle.
side = radius*np.sqrt(3)

sims = 10000000
#Randomizing points on the circle. Performing the same randomization on the x and y of one point.
rand1 = np.random.choice(x.size,size = (sims))
rand2 = np.random.choice(x.size,size = (sims))

p1x = x[rand1]
p1y = y[rand1]
p2x = x[rand2]
p2y = y[rand2]

#Finding the length of each random chord.
length = np.sqrt(np.square(p1x-p2x)+np.square(p1y-p2y))

print("The answer to part 4.a is:", np.sum(length>side)/sims)