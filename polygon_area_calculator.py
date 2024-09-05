import sys


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if (self.width >= 50) or (self.height >= 50):
            return 'Too big for picture.'
        else:
            row = ('*'*(self.width) + '\n') * self.height
            return str(row)

    def get_amount_inside(self, shape):
        times = 0
        if (self.width > shape.width) and (self.height > shape.height):
            times = (self.width*self.height)//(shape.width*shape.height)
            return times
        else:
            return 0


class Square (Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, side):
        self.side = side

    def set_width(self, side):
        self.side = side

    def set_height(self, side):
        self.side = side

    def get_diagonal(self):
        return ((self.side ** 2 + self.side ** 2) ** .5)

    def get_picture(self):
        if self.side >= 50:
            return 'Too big for picture.'
        else:
            row = ('*'*(self.side) + '\n') * self.side
            return str(row)


arguments = sys.argv
print(arguments)

# Examples
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(3)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(7)
rect.set_width(16)
print(rect.get_amount_inside(sq))
