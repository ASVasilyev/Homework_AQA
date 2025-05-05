from figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        if radius <=0:
            raise ValueError ("Circle radius can't be less than 0")
        self.radius = radius

    @property
    def area(self):
        return self.radius ** 2 * 3.14

    @property
    def perimetr(self):
        return self.radius * 2 * 3.14