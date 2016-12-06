import numpy as np

# Taking a random radius
radius = np.random.randint(1,100)

# No. of points inside the circle
n = 1000000

"""
Creating the points that lie in the square of side 2r 
Assuming circle to be centered at (0,0).
"""
def Points(r,n):

	x = np.random.uniform(-r,r,size = n)
	y = np.random.uniform(-r,r,size = n)

	return x, y

x,y = Points(radius,1000000)

#Finding the location of points which are outside the circle and deleting them
outside = np.where(np.sqrt(np.square(x) + np.square(y))>radius)

x = np.delete(x,outside)
y = np.delete(y,outside)

permutation1 = np.random.permutation(x.size)
permutation2 = np.random.permutation(x.size)

x1 = x[permutation1]
y1 = y[permutation1]
x2 = y[permutation2]
y2 = y[permutation2]

# Distance between point1 and center, point2 and center, distance between points.
dist1 = np.sqrt(np.square(x1)+np.square(y1))
dist2 = np.sqrt(np.square(x2)+np.square(y2))
l = np.sqrt(np.square(x1-x2) + np.square(y1-y2))

# Finding height of the triangle. This is the distance from midpoint of the chord to centre.
s = (dist1 + dist2 + l)/2
area = np.sqrt(s*(s - dist1) * (s - dist2) * (s - l))
height = 2 * area / l

# Calculating Chord length
chord = np.sqrt(np.square(radius)-np.square(height))*2
side = radius*np.sqrt(3)

print("\n\n\nThe answer to 4.c is:",np.sum(chord>side)/x.size)
