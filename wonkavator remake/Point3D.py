class Point3D:
    def __init__(self, x, y, z):  # class constructor
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __eq__(self, other):  # comparison
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):  # string representation
        return "<{}, {}, {}>".format(self.x, self.y, self.z)

    def add(self, other):  # add two points together
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def distance(self, other):  # get distance between two point
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    def sign(x):
        # Return the sign of x (0 if x is 0).
        if x > 0:  # x positive
            return 1
        elif x < 0:  # x negative
            return -1
        else:  # x zero
            return 0

    def get_direction_vector(self, other):
        # Return a vecotr of 1, 0 or -1 in each dimension corresponding to
        # the direction you would have to move from the self point to get to the other point.
        def sign(x):
            # Return the sign of x (0 if x is 0).
            if x > 0:  # x positive
                return 1
            elif x < 0:  # x negative
                return -1
            else:  # x zero
                return 0

        return Point3D(
            sign(other.x - self.x), sign(other.y - self.y), sign(other.z - self.z)
        )

    def aslist(self):  # Return the Point2D object as a list of three numbers.
        return [self.x, self.y, self.z]


def get_random_point(x0, x1, y0, y1, z0, z1):
    # return a Point3D object with random coordinates within the given x,y,z intervals.
    return Point3D(randint(x0, x1), randint(y0, y1), randint(z0, z1))
