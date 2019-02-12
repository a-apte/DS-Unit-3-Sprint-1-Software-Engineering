class Rectangle:
# This class instantiates a rectangle
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
# The Square class inherits from the Rectangle Class as a square is a type of rectangle.
    def __init__(self, side):
        super().__init__(side, side)
		
class Cube(Square):
# The Cube class inherits from Square to compute surface area and volume
    def surface_area(self):
        return super().area() * 6

    def volume(self):
        return self.length * self.length * self.length