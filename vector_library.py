"""create a library for vector operations"""

from math import sqrt

class Vector():
    """create vectors - initialize instances by entering a list as coordinates (2Dimensional)"""
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add_vector(self, vector2):
        """add vector2 to the vector your called the method on"""
        new_coordinates = [x+y for x, y in zip(self.coordinates, vector2.coordinates)]
        return Vector(new_coordinates)

    def sub_vector(self, vector2):
        """subtract vector2 from the vector your called the method on"""
        new_coordinates = [x-y for x, y in zip(self.coordinates, vector2.coordinates)]
        return new_coordinates

    def times_scalar(self, scalar):
        """multiply the vector your called the method on with the inputted scalar"""
        new_coordinates = [x*scalar for x in self.coordinates]
        return new_coordinates

    def get_magnitude(self):
        "get the magnitude of the vector"
        magnitude = sqrt(sum([x**2 for x in self.coordinates]))
        return magnitude

    def normalize(self):
        "get the normalized vector of the vector you called the method on"
        try:
            normal_coord = [x/self.get_magnitude() for x in self.coordinates]
            return Vector(normal_coord)
        except ZeroDivisionError:
            raise Exception("Cannot normalize vectors with zero magnitude")

    def get_dot_prod(self, vector2):
        dot_prod = [x*y for x, y in zip(self.coordinates, vector2.coordinates)]
        dot_prod = sum(dot_prod)
        return dot_prod

# -----------testing---------------
vector_1 = Vector([1, 2, -1])
vector_2 = Vector([3, 1, 0])

print(vector_1.get_dot_prod(vector_2))
