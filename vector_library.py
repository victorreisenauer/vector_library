"""create a library for vector operations"""

from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector():
    """create vectors - initialize instances by entering a list as coordinates (2Dimensional)"""
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def is_zero(self, tolerance=1e-10):
        return self.get_magnitude() < tolerance

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
        new_coordinates = [x*Decimal(scalar) for x in self.coordinates]
        return new_coordinates

    def get_magnitude(self):
        """get the magnitude of the vector"""
        magnitude = Decimal(sqrt(sum([x**2 for x in self.coordinates])))
        return magnitude

    def normalize(self):
        """get the normalized vector of the vector you called the method on"""
        try:
            normal_coord = [x/self.get_magnitude() for x in self.coordinates]
            return Vector(normal_coord)
        except ZeroDivisionError:
            raise Exception("Cannot normalize vectors with zero magnitude")

    def get_dot_prod(self, vector2):
        """get the dot product(inner product) instance and vector2"""
        return sum([x*y for x, y in zip(self.coordinates, vector2.coordinates)])

    def get_angle(self, vector2, in_degrees=False):
        """get the angle between the instance and vector2"""
        try:
            u1 = self.normalize()
            u2 = vector2.normalize()
            angle_in_radians = acos(u1.get_dot_prod(u2))

            if in_degrees:
                return degrees(angle_in_radians)
            return angle_in_radians
        except Exception as zero_error:
            if str(zero_error) == "Cannot normalize vectors with zero magnitude":
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise zero_error

    def is_orthogonal_to(self, vector2, tolerance=1e-10):
        """check if instance is orthogonal (90 degrees) to vector2"""
        return abs(self.get_dot_prod(vector2)) < tolerance

    def is_parallel_to(self, vector2):
        """check if instance is parallel to vector2"""
        return (self.is_zero()
                or vector2.is_zero()
                or self.get_angle(vector2) == 0
                or self.get_angle(vector2) == pi)



# -----------testing---------------
vector_1 = Vector(['1', '0'])
vector_2 = Vector(['0', '5'])

#print(vector_2.is_parallel_to(vector_1))
