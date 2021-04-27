class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        s = ''
        for _ in range(self.height):
            s += '*' * self.width + '\n'
        return s

    def get_amount_inside(self, other):
        return self.width // other.width * self.height // other.height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, lenght):
        self.width = self.height = lenght

    def set_side(self, lenght):
        self.width = self.height = lenght

    def set_width(self, lenght):
        self.set_side(lenght)

    def set_height(self, lenght):
        self.set_side(lenght)

    def __str__(self):
        return f'Square(side={self.width})'
