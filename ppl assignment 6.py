import turtle

sai = turtle.getscreen()
tom = turtle.Turtle()
w = turtle.Screen()
tom.hideturtle()

class shape:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length


class point(shape):
    def draw(self):
        tom.color("black")
        tom.shape("circle")
        tom.forward(self.length)
    def info(self):
        print("This is a point")


class line(shape):
    def draw(self):
        tom.color("black")
        tom.shape("arrow")
        tom.forward(self.length)
    def info(self):
        print("This is a line with length %s"%(self.length))


class polygon(shape):
    def defination(self):
        print("This is one of the example of polynomial")
    def info(self):
        print("This is a polygon with total number of sides %s & length of each side is %s"%(self.sides,self.length))


class triangle(polygon):
    def draw(self):
        tom.color("red")
        tom.shape("turtle")
        tom.begin_fill()
        tom.fillcolor("yellow")
        tom.circle(self.length, steps=self.sides)
        tom.end_fill()
        tom.hideturtle()


class square(polygon):
    def draw(self):
        tom.color("blue")
        tom.shape("classic")
        tom.begin_fill()
        tom.fillcolor("red")
        tom.circle(self.length, steps=self.sides)
        tom.end_fill()
        tom.hideturtle()


class pentagon(polygon):
    def draw(self):
        tom.color("black")
        tom.shape("turtle")
        tom.begin_fill()
        tom.fillcolor("blue")
        tom.circle(self.length, steps=self.sides)
        tom.end_fill()
        tom.hideturtle()


class hexagon(polygon):
    def draw(self):
        tom.color("orange")
        tom.shape("square")
        tom.begin_fill()
        tom.fillcolor("black")
        tom.circle(self.length, steps=self.sides)
        tom.end_fill()
        tom.hideturtle()


class octagon(polygon):
    def draw(self):
        tom.color("yellow")
        tom.shape("triangle")
        tom.begin_fill()
        tom.fillcolor("green")
        tom.circle(self.length, steps=self.sides)
        tom.end_fill()
        tom.hideturtle()


class circle(shape):
    def draw(self):
        w.bgcolor("black")
        tom.color("white")
        tom.shape("turtle")
        tom.begin_fill()
        tom.fillcolor("white")
        tom.circle(self.length)
        tom.end_fill()
        tom.hideturtle()
    def info(self):
        print("This is a circle with radius %s"%(self.length))

m = circle(0, 100)  #m is an object belonging to class shape
m.draw()
m.info()
