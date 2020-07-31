import math
from random import randint
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from Factory import Factory
from Person import Person
from Point3D import Point3D
from Wonkavator import Wonkavator


def explode(data):
    size = np.array(data.shape) * 2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e


structure = np.zeros((5, 5, 5), dtype=bool)
filled = np.ones(structure.shape)
facecolors = np.where(structure, "#FFD65DC0", "#7A88CCC0")
edgecolors = np.where(structure, "#BFAB6E", "#7D84A6")
# upscale the above voxel image, leaving gaps
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)

plt.ion()  # enable interactive mode (continue graphing without having to close the window)
plt.show()  # show the plot


def sign(x):
    # Return the sign of x (0 if x is 0).
    if x > 0:  # x positive
        return 1
    elif x < 0:  # x negative
        return -1
    else:  # x zero
        return 0


def get_random_point(x0, x1, y0, y1, z0, z1):
    # return a Point3D object with random coordinates within the given x,y,z intervals.
    return Point3D(randint(x0, x1), randint(y0, y1), randint(z0, z1))


if __name__ == "__main__":
    factory_size = Point3D(5, 5, 5)
    # people[0] = Person("Candice", (3, 4, 0), (2, 0, 1))
    # people[1] = Person("Andy", (4, 3, 0), (4, 3, 1))
    # people[2] = Person("Belle", (1, 3, 4), (3, 1, 1))
    # people[3] = Person("Cecily", (1, 3, 4), (3, 0, 1))
    # people[4] = Person("Angela", (1, 0, 1), (4, 2, 1))
    # people[5] = Person("Thornton", (2, 3, 2), (0, 1, 4))
    # people[6] = Person("Sheryl", (0, 1, 0), (1, 0, 1))
    # people[7] = Person("Benny", (2, 1, 2), (2, 1, 3))
    # create the elevator

    people = [
        ("Name:Candice", "cur:" <4, 0, 2>, "dst:"<4, 0, 3>), 
        ("Name:Murray", "cur:"<3, 2, 4>, "dst:"<4, 1, 4>),
        ('Name:Belle', 'cur:'<2, 2, 2>, 'dst:'<2, 2, 0>),
        ('Name:Cecily', 'cur:' <3, 0, 1>, 'dst:'<2, 1, 0>),
        ('Name:Angela', 'cur:' <2, 2, 3>, 'dst:'<2, 3, 4>), 
        ('Name:Thornton', 'cur:' <3, 0, 3>, 'dst:'<3, 2, 4>), 
        ('Name:Sheryl', 'cur:' <3, 3, 2>, 'dst:'<3, 2, 1>), 
        ('Name:Benny', 'cur:' <4, 4, 3>, 'dst:'<3, 0, 3>)]


    elevator = Wonkavator(factory_size)

    # create the factory

    factory = Factory(factory_size, people, elevator)

    while True:
        factory.run()
        factory.show()

        # check if everyone has arrived at their destinations
        if factory.is_finished():
            break

    print("Everyone has arrived.")
