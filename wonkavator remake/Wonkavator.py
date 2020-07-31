from Point3D import Point3D


def sign(x):
    # Return the sign of x (0 if x is 0).
    if x > 0:  # x positive
        return 1
    elif x < 0:  # x negative
        return -1
    else:  # x zero
        return 0


class Wonkavator:
    def __init__(self, factory_size):  # class constructor
        # 1) current elevator position in structure
        self.cur_pos = Point3D(0, 0, 0)  # calling class Point3D
        self.factory_size = factory_size  # 2) the dimension of the structure/factory
        self.people_in_elevator = []  # 3) the list of people currently in the elevator

    def move(self, people):  # move the elevator
        # get the direction in which to move
        direction = self.choose_direction(people)
        # check if the direction is correct
        if any(not isinstance(d, int) for d in direction.aslist()):
            raise ValueError("Direction values must be integers.")
        if any(abs(d) > 1 for d in direction.aslist()):
            raise ValueError("Directions can only be 0 or 1 in any dimension.")
        if all(d == 0 for d in direction.aslist()):
            raise ValueError(
                "The elevator cannot stay still (direction is 0 in all dimensions)."
            )
        if any(
            d < 0 or d > s
            for d, s in zip(
                self.cur_pos.add(direction).aslist(), self.factory_size.aslist()
            )
        ):
            raise ValueError("The elevator cannot move outside the bounds of the grid.")

        # move the elevator in the correct direction
        self.cur_pos = self.cur_pos.add(direction)

    def choose_direction(self, people):
        # Return the direction in which to move, as a Point3D object.
        print("Elevator Position: " + str(self.cur_pos), end=" ")
        for p in people:
            if p in self.people_in_elevator:
                print(
                    p.name
                    + " is in elevator and going to destination "
                    + str(p.dst_pos)
                )
                return self.cur_pos.get_direction_vector(p.dst_pos)
            elif p.arrived == False:
                print(
                    "Evalator is travelling to pick up "
                    + p.name
                    + " at "
                    + str(p.cur_pos)
                )
                return self.cur_pos.get_direction_vector(p.cur_pos)
            else:
                pass

    def person_enters(self, person):  # person arrives in elevator
        print(person.name + "  has entered the elevator " + str(person.cur_pos))
        if person.arrived:
            raise Exception(
                "A person can only enter the elevator if they have not yet reached their destination."
            )
        self.people_in_elevator.append(person)  # add them to the list

    def person_leaves(self, person):  # person departs elevator
        if person.dst_pos != elevator.cur_pos:
            raise Exception(
                "A person can only leave the elevator if the elevator has reached their destination point."
            )

        person.arrive_at_destination()  # let the person know they have arrived
        print(
            person.name
            + "  has arrived and exited at destination "
            + str(person.cur_pos)
        )
        self.people_in_elevator.remove(person)  # remove them from the list

