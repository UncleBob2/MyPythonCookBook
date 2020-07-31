import math
from random import randint
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e


structure = np.zeros((5, 5, 5), dtype=bool)
filled = np.ones(structure.shape)
facecolors = np.where(structure, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(structure, '#BFAB6E', '#7D84A6')
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


class Point3D():
    def __init__(self, x, y, z):  # class constructor
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __eq__(self, other):  # comparison
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):  # string representation
        return '<{}, {}, {}>'.format(self.x, self.y, self.z)

    def add(self, other):  # add two points together
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def distance(self, other):  # get distance between two point
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def get_direction_vector(self, other):
        # Return a vecotr of 1, 0 or -1 in each dimension corresponding to
        # the direction you would have to move from the self point to get to the other point.
        return Point3D(sign(other.x - self.x), sign(other.y - self.y), sign(other.z - self.z))

    def aslist(self):  # Return the Point2D object as a list of three numbers.
        return[self.x, self.y, self.z]


def get_random_point(x0, x1, y0, y1, z0, z1):
    # return a Point3D object with random coordinates within the given x,y,z intervals.
    return Point3D(randint(x0, x1), randint(y0, y1), randint(z0, z1))


class Person:
    '''
    The Person class defines a person inside the building. At the start of the simulation, each Person will be located at one particular (x, y, z) coordinate in the grid, and will want to travel to some other (x, y, z) coordinate.'''

    def __init__(self, name, cur_pos, dst_pos):
        # Class constructor with 4 attribute
        self.name = name  # 1) name
        self.cur_pos = cur_pos  # 2) current position
        self.dst_pos = dst_pos  # 3) destination positon
        self.arrived = False  # 4) whether arrived at final destination

    def arrive_at_destination(self):
        self.cur_pos = self.dst_pos
        self.arrived = True

    def __str__(self):  # string representation
        return "Name:" + self.name + "; cur: " + str(self.cur_pos) + "; dst:" + str(self.dst_pos)


class Factory:
    '''The Factory class contains methods to run the simulation and display it to the screen. It also contains four attributes: the size of the factory (a Point3D object), a list of the people in the simulation (i.e., a list of Person objects), one object of type Wonkavator for the actual elevator, and finally an attribute relating to the Matplotlib visualization.'''

    def __init__(self, factory_size, people, elevator):  # class constructor with 4 attributes
        self.factory_size = factory_size  # dimension of structure/factory
        self.people = people  # 2) list of people
        self.elevator = elevator  # the wonkavator elevator
        # self.axes = plt.axes(projection='3d')  # Mathplotlib visulation
        fig = plt.figure()
        self.axes = fig.gca(projection='3d')

    def run(self):
        if not self.is_finished():
            self.elevator.move(self.people)
            for p in self.people:
                if p in self.elevator.people_in_elevator and p.dst_pos == self.elevator.cur_pos:
                    self.elevator.person_leaves(p)
                elif p.cur_pos == self.elevator.cur_pos and p.arrived == False:
                    self.elevator.person_enters(p)
    '''
    When you run, you will see a visualization of the 3D grid on- screen. (This visualization uses Matplotlib!) The elevator will appear as a green dot and the people will appear as blue dots. As you write code for the other methods, you will see the elevator (green dot) begin to move around the grid. Once the elevator picks up a person, a red dot will appear on the grid, indicating the person's destination. The red dot will disappear when the elevator travels to that location and drops off the person. Here is a sample visualization: (To stop the simulation and close the visualization window, press the Stop button in the Thonny toolbar.)

    '''

    def show(self):  # display the grid
        self.axes.clear()  # clear the previous window contents

        # set the axis bounds
        self.axes.set_xlim(0, factory_size.x)
        self.axes.set_ylim(0, factory_size.y)
        self.axes.set_zlim(0, factory_size.z)
        self.axes.set_xticks(list(range(factory_size.x + 1)))
        self.axes.set_yticks(list(range(factory_size.y + 1)))
        self.axes.set_zticks(list(range(factory_size.z + 1)))

        # show a blue dot for each person not yet in the elevator / not yet arrived at their destination
        xs, ys, zs = [], [], []
        for person in self.people:
            if not person.arrived and person not in self.elevator.people_in_elevator:
                xs.append(person.cur_pos.x)
                ys.append(person.cur_pos.y)
                zs.append(person.cur_pos.z)
        self.axes.scatter3D(xs, ys, zs, color='blue')
        # self.axes.voxels(xs, ys, zs, filled_2,facecolors = fcolors_2, edgecolors = ecolors_2)

        # show a red dot for the destinations of the people currently in the elevator
        edxs, edys, edzs = [], [], []
        for person in self.people:
            if person in self.elevator.people_in_elevator:
                edxs.append(person.dst_pos.x)
                edys.append(person.dst_pos.y)
                edzs.append(person.dst_pos.z)
        self.axes.scatter3D(edxs, edys, edzs, color='red')
        # self.axes.voxels(edxs, edys, edzs, filled_2,
        #                  facecolors='red', edgecolors='red')

        # show a green dot for the elevator itself
        self.axes.scatter3D([self.elevator.cur_pos.x], [self.elevator.cur_pos.y], [
            self.elevator.cur_pos.z], color='green')
        # self.axes.voxels([self.elevator.cur_pos.x], [self.elevator.cur_pos.y], [
        # self.elevator.cur_pos.z],
        # facecolors='green', edgecolors='green')

        plt.draw()
        plt.pause(0.5)

    def is_finished(self):
        return all(person.arrived for person in self.people)


class Wonkavator:
    '''The Wonkavator class contains three attributes: its current position in the grid (represented as a Point3D object), the size of the factory (represented as a Point3D object), and a list of the people currently in the Wonkavator. •'''

    def __init__(self, factory_size):  # class constructor
        # 1) current elevator position in structure
        self.cur_pos = Point3D(0, 0, 0)
        self.factory_size = factory_size  # 2) the dimension of the structure/factory
        self.people_in_elevator = []  # 3) the list of people currently in the elevator

    def move(self, people):  # move the elevator
        '''
        The Wonkavator class contains methods to move the Wonkavator and maintain the list of people currently inside. The Wonkavator must travel to each person's (x, y, z) coordinate, moving by at most 1 in any dimension at a time (as described above). After picking up a person, it must deliver them to their destination (x, y, z) coordinate. (Note: The Wonka- vator doesn't have to deliver a person right after picking them up, it could pick up multiple people before delivering all of them to their destinations.) Once a person has reached their destination, they remain there for the rest of the simulation. The Wonkavator class contains three attributes: its current position in the grid (represented as a Point3D object), the size of the factory represented as a Point3D object), and a list of the people currently in the Wonkavator. The Factory class contains methods to run the simulation and display it to the screen. It also contains four attributes: the size of the factory a Point3D object), a list of the people in the simulation (i.e., a list of Person objects), one object of type Wonkavator for the actual elevator, and finally an attribute relating to the Matplotlib visualization. Much of the code for these three classes has already been provided to you in the given wonkavator.py file. Your job is to write one incomplete method of each of the three classes, as listed on the next page.


        '''
        # get the direction in which to move
        direction = self.choose_direction(people)
        # check if the direction is correct
        if any(not isinstance(d, int) for d in direction.aslist()):
            raise ValueError("Direction values must be integers.")
        if any(abs(d) > 1 for d in direction.aslist()):
            raise ValueError("Directions can only be 0 or 1 in any dimension.")
        if all(d == 0 for d in direction.aslist()):
            raise ValueError(
                "The elevator cannot stay still (direction is 0 in all dimensions).")
        if any(d < 0 or d > s for d, s in zip(self.cur_pos.add(direction).aslist(), self.factory_size.aslist())):
            raise ValueError(
                "The elevator cannot move outside the bounds of the grid.")

        # move the elevator in the correct direction
        self.cur_pos = self.cur_pos.add(direction)

    def choose_direction(self, people):
        # Return the direction in which to move, as a Point3D object.
        print("Elevator Position: " + str(self.cur_pos), end=" ")
        for p in people:
            if p in self.people_in_elevator:
                print(
                    p.name + " is in elevator and going to destination " + str(p.dst_pos))
                return self.cur_pos.get_direction_vector(p.dst_pos)
            elif p.arrived == False:
                print("Evalator is travelling to pick up " +
                      p.name + " at " + str(p.cur_pos))
                return self.cur_pos.get_direction_vector(p.cur_pos)
            else:
                pass

    def person_enters(self, person):  # person arrives in elevator
        print(person.name + "  has entered the elevator " + str(person.cur_pos))
        if person.arrived:
            raise Exception(
                "A person can only enter the elevator if they have not yet reached their destination.")
        self.people_in_elevator.append(person)  # add them to the list

    def person_leaves(self, person):  # person departs elevator
        if person.dst_pos != elevator.cur_pos:
            raise Exception(
                "A person can only leave the elevator if the elevator has reached their destination point.")

        person.arrive_at_destination()  # let the person know they have arrived
        print(person.name + "  has arrived and exited at destination " +
              str(person.cur_pos))
        self.people_in_elevator.remove(person)  # remove them from the list


if __name__ == '__main__':
    factory_size = Point3D(5, 5, 5)
    # create the people objects
    people = []
    for name in ["Candice", "Andy", "Belle", "Cecily", "Angela", "Thor", "Sherryl", "Benny"]:
        cur = get_random_point(0, factory_size.x - 1, 0,
                               factory_size.y - 1, 0, factory_size.z - 1)
        dst = get_random_point(0, factory_size.x - 1, 0,
                               factory_size.y - 1, 0, factory_size.z - 1)
        people.append(Person(name, cur, dst))

    # create the elevator
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

'''
Programming can be very useful because it can simulate real-world environments. In this question we will write some code to complete a Python simulation of a Wonkavator. A Wonkavator is like an elevator, but an elevator can only go up and down. A Wonkavator can go sideways, and slantways, and longways, and backways, amongst other things. In fact, it can take you to any room in an entire building. We will simulate a building in which the Wonkavator will move around. The building will be represented by a 3D grid, where each coordinate in the grid represents a room. The Wonkavator can travel from room to room by moving at most 1 unit in any direction. For example, it could move from point (2, 3, 4) to point (2, 4, 5), by making a movement of (0, 1, 1). However, it is illegal to make a move from (1, 1, 1) to (3, 1, 1), as we can move a maximum of 1, not 2, in any direction. A move of (0, 0, 0) (i.c., staying in place) is also invalid. Further, it is invalid to move beyond the bounds of the grid (i.c., out of the building). If the Wonkavator is at coordinate (5, 5, 4), and the grid is of size 6x6x6, then it is invalid to move in the direction (1, 0, 0), as that would bring the Wonkavator out of the grid. In the code provided to you, three classes are defined: Person, Factory and Wonkavator: • The Person class defines a person inside the building. At the start of the simulation, each Person will be located at one particular (x, y, z) coordinate in the grid, and will want to travel to some other (x, y, z) coordinate. The Person class contains four attributes: the person's name, their current position in the grid (represented as a Point3D object), their destination position in the grid (represented as a Point3D object), and finally a boolean variable indicating whether or not they have arrived at their destination yet. • The Wonkavator class contains methods to move the Wonkavator and maintain the list of people currently inside. The Wonkavator must travel to each person's (x, y, z) coordinate, moving by at most 1 in any dimension at a time (as described above). After picking up a person, it must deliver them to their destination (x, y, z) coordinate. (Note: The Wonka- vator doesn't have to deliver a person right after picking them up, it could pick up multiple people before delivering all of them to their destinations.) Once a person has reached their destination, they remain there for the rest of the simulation. The Wonkavator class contains three attributes: its current position in the grid (represented as a Point3D object), the size of the factory represented as a Point3D object), and a list of the people currently in the Wonkavator. The Factory class contains methods to run the simulation and display it to the screen. It also contains four attributes: the size of the factory a Point3D object), a list of the people in the simulation (i.e., a list of Person objects), one object of type Wonkavator for the actual elevator, and finally an attribute relating to the Matplotlib visualization. Much of the code for these three classes has already been provided to you in the given wonkavator.py file. Your job is to write one incomplete method of each of the three classes, as listed on the next page.
Name: _init_method of Person class Parameters: In addition to self, a string name, Point3D object cur-pos and Point3D object dst-pos. What it should do: Create four attributes: name, cur_pos, dst_pos and arrived. The first three attributes should be assigned the values of the respective parameters, while the arrived attribute should be set to False. Name: run method of Factory class Parameters: No parameters (just self). What it should do: This method is the main loop for the simulation. It checks to see if the elevator is currently in a room where there are people who want to enter the elevator, and/or if there are people in the elevator whose destination point is the current room and who thus want to leave the elevator. If there is a person(s) who are in the same room as the elevator and need to be picked up, then, for each such person, the person_enters method of the elevator attribute should be called, with the person passed as argument to the method. However, make sure that the person does need to be picked up and has not already arrived at their destination room (you can check the arrived method of the person - if it is True, then they should not be picked up as they have already arrived). If there is a person(s) who are in the elevator and whose destination is the current room, and thus need to be dropped off in the room, the person leaves method of the elevator attribute should be called, with the person passed as argument to the method. (Hint: Whenever writing a new method for a class, consider what attributes of the class you might need to use in the method. There may be many attributes, so it's good to focus only on the ones you need. For example, here you may need to access the people attribute, perhaps using a for loop to go through each Person object in that list. You may also need to use in some way the people_inelevator and cur-pos attributes of the elevator attribute.) Finally, the method should call the move method of the elevator attribute, and pass the list of people (self.people) as argument. (This line is already done for you.) Name: choose_direction method of Wonkavator class Parameters: In addition to self, people: a list of Person objects What it should do: This method tells the elevator in which direction to move, by returning a Point3D object with the direction to move in each dimension. The elevator can only move a maximum of 1 unit in any dimension, so each component of the direction must be either -1, 0, or 1. (Note that a direction of (0, 0, 0) is invalid as the elevator cannot stay in the same place, but a direction of (1, 1,-1) is fine.) There is no constraint in how this method should be designed, but the simulation must end with all people taken to their destinations. Thus, the method should return a direction such that it moves
closer either to picking up a person or dropping off a person, so that in the end, the simulation can finish. (Hint: The get direction vector method of the Point3D class may be useful to you here Given two Point3D objects x and y, calling x.get direction vector (y) will return a direction vector of one unit in each dimension from x moving towards y.) Filename You must write these methods in a file called wonkavator.py. The three methods are already defined for you, as are all the other methods of the classes - do not alter any code except for the three methods listed. Examples (as executed in Thonny) Once you complete the first method (the _init_method of the Person class), as well as return some kind of Point3D object in the choose_direction method of Wonkavator class, you will be able to run the code file in Thonny. When you run, you will see a visualization of the 3D grid on- screen. (This visualization uses Matplotlib!) The elevator will appear as a green dot and the people will appear as blue dots. As you write code for the other methods, you will see the elevator (green dot) begin to move around the grid. Once the elevator picks up a person, a red dot will appear on the grid, indicating the person's destination. The red dot will disappear when the elevator travels to that location and drops off the person. Here is a sample visualization: (To stop the simulation and close the visualization window, press the Stop button in the Thonny toolbar.) 
'''
