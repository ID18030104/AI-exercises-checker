import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, area: {self.area:.2f}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("Can only add another Circle")

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

def draw_circles(circles):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    x_pos = -300

    for circle in circles:
        turtle.goto(x_pos, 0 - circle.radius)  
        turtle.pendown()
        turtle.circle(circle.radius)
        turtle.penup()
        x_pos += circle.radius * 2 + 10  

    turtle.done()


c1 = Circle(radius=30)
c2 = Circle(diameter=40)
c3 = Circle(radius=10)
c4 = c1 + c2
c5 = Circle(radius=20)

circles = [c1, c2, c3, c4, c5]
circles.sort()


for c in circles:
    print(c)


draw_circles(circles)