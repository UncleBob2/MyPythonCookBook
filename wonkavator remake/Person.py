class Person:
    """
    The Person class defines a person inside the building. At the start of the simulation, each Person will be located at one particular (x, y, z) coordinate in the grid, and will want to travel to some other (x, y, z) coordinate."""

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
        return (
            "Name:"
            + self.name
            + "; cur: "
            + str(self.cur_pos)
            + "; dst:"
            + str(self.dst_pos)
        )
