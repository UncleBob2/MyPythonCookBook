class Show:
    def __init__(
        self, factory_size, people, elevator
    ):  # class constructor with 4 attributes
        self.factory_size = factory_size  # dimension of structure/factory
        self.people = people  # 2) list of people
        self.elevator = elevator  # the wonkavator elevator
        # self.axes = plt.axes(projection='3d')  # Mathplotlib visulation
        fig = plt.figure()
        self.axes = fig.gca(projection="3d")

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
        self.axes.scatter3D(xs, ys, zs, color="blue")
        # self.axes.voxels(xs, ys, zs, filled_2,facecolors = fcolors_2, edgecolors = ecolors_2)

        # show a red dot for the destinations of the people currently in the elevator
        edxs, edys, edzs = [], [], []
        for person in self.people:
            if person in self.elevator.people_in_elevator:
                edxs.append(person.dst_pos.x)
                edys.append(person.dst_pos.y)
                edzs.append(person.dst_pos.z)
        self.axes.scatter3D(edxs, edys, edzs, color="red")
        # self.axes.voxels(edxs, edys, edzs, filled_2,
        #                  facecolors='red', edgecolors='red')

        # show a green dot for the elevator itself
        self.axes.scatter3D(
            [self.elevator.cur_pos.x],
            [self.elevator.cur_pos.y],
            [self.elevator.cur_pos.z],
            color="green",
            label="elevator",
        )
        # self.axes.voxels([self.elevator.cur_pos.x], [self.elevator.cur_pos.y], [
        # self.elevator.cur_pos.z],
        # facecolors='green', edgecolors='green')

        plt.draw()
        plt.pause(1)

    def is_finished(self):
        return all(person.arrived for person in self.people)
