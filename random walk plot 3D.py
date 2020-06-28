
import matplotlib.pyplot as plt  # import the 3d package
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import random

XYZ_cord = [(0, 0, 0)]  # declare origin as 0,0,0


def walk():
    '''Creating six directionals random walk'''
    x, y, z = 0, 0, 0  # declare multiple variables in python

    path = random.choice(['North', 'South', 'West', 'East', 'Up', 'Down'])
    if path == 'North':
        y = y + 1
    if path == 'South':
        y = y - 1
    if path == 'West':
        x = x + 1
    if path == 'East':
        x = x - 1
    if path == 'Up':
        z = z + 1
    if path == 'Down':
        z = z - 1
    return(x, y, z)  # returning 1 selected choice in the 3 possible direction


for x in range(10_000):  # the number of walk that we would like to perform
    result = walk()  # calling the walk function to perform the random walk
    # calling the previous cordinate, our initial origin is defined as 0,0,0 tuple
    tuplex = (XYZ_cord[-1])
    # extract the previous x axis from the xyz coordinates tuple
    x_old = tuplex[0]
    y_old = tuplex[1]  # exgract the previous y axis
    z_old = tuplex[2]  # extract the previous z axis
    # combine previous x axis with new random walk result
    x_new = result[0] + x_old
    # combine previous y axis with new random walk result
    y_new = result[1] + y_old
    z_new = result[2] + z_old
    # add the new coordinate x,y,z coordinate to the list
    XYZ_cord.append([x_new, y_new, z_new])


# unzipping the list of coordinates using zip() along with the unpacking operator * => zip(* ___)

x, y, z = zip(*XYZ_cord)

fig = plt.figure()  # to create 3D plot, we create and assign a figure object. This will allow us greater opportunity for plot customization
# from the figure object we are going to create a subplot. This will allow us to have specific access to all the properties of the figure. The 111 => 1 row, 1 colum, 1st position
N = len(z)
plot1 = fig.add_subplot(111, projection='3d')
plot1.set_xlabel('X Label')
plot1.set_ylabel('Y Label')
plot1.set_zlabel('Z Label')
plot1.scatter(x, y, z, c=plt.cm.jet(np.linspace(0, 1, N)))


plot2 = fig.add_subplot(122, projection='3d')
plot2.set_xlabel('X Label')
plot2.set_ylabel('Y Label')
plot2.set_zlabel('Z Label')
plot2.plot3D(x, y, z, c='blue')


plt.show()
