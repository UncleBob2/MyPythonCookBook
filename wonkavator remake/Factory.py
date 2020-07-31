import matplotlib.pyplot as plt


class Factory:
    """The Factory class contains methods to run the simulation and display it to the screen. It also contains four attributes: the size of the factory (a Point3D object), a list of the people in the simulation (i.e., a list of Person objects), one object of type Wonkavator for the actual elevator, and finally an attribute relating to the Matplotlib visualization."""

    def __init__(
        self, factory_size, people, elevator
    ):  # class constructor with 4 attributes
        self.factory_size = factory_size  # dimension of structure/factory
        self.people = people  # 2) list of people
        self.elevator = elevator  # the wonkavator elevator
        # self.axes = plt.axes(projection='3d')  # Mathplotlib visulation
        fig = plt.figure()
        self.axes = fig.gca(projection="3d")

    def run(self):
        if not self.is_finished():
            self.elevator.move(self.people)
            for p in self.people:
                if (
                    p in self.elevator.people_in_elevator
                    and p.dst_pos == self.elevator.cur_pos
                ):
                    self.elevator.person_leaves(p)
                elif p.cur_pos == self.elevator.cur_pos and p.arrived == False:
                    self.elevator.person_enters(p)

    """
    When you run, you will see a visualization of the 3D grid on- screen. (This visualization uses Matplotlib!) The elevator will appear as a green dot and the people will appear as blue dots. As you write code for the other methods, you will see the elevator (green dot) begin to move around the grid. Once the elevator picks up a person, a red dot will appear on the grid, indicating the person's destination. The red dot will disappear when the elevator travels to that location and drops off the person. Here is a sample visualization: (To stop the simulation and close the visualization window, press the Stop button in the Thonny toolbar.)

    """

