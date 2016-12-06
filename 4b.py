import numpy as np

radius = np.random.randint(1,100)

# No. of points in an 2r*2r square
n = 1000000

"""
Creating a square of side 2r.
"""
def Points(r,n):

	x = np.random.uniform(-r,r,size = n)
	y = np.random.uniform(-r,r,size = n)

	return x, y

x, y = Points(radius,1000000)

# Finding the location of points which are outside the circle and deleteing them.
outside = np.where(np.sqrt(np.square(x) + np.square(y))>radius)

x = np.delete(x,outside)
y = np.delete(y,outside)

# The distance of each point from the center. If <r/2, then the chord will be longer.
dist = np.sqrt(np.square(x)+np.square(y))

sims = 100000000
# Choosing a few random points in the circle. More precisely, their distance from the centre
rand_dist = np.random.choice(dist,size = (sims,))

print("The answer to 4.b is:",np.sum(rand_dist<radius/2)/sims)
