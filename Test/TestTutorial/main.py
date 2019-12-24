import turtle

# Tutorial 1: Create Variables
a = 1;
b = "Hello World";
print(a);
print(b);

# Tutorial 2: Create Functions
def createSquare():
    myTurtle = turtle.Turtle();
    myTurtle.forward(100);
    myTurtle.right(90);
    myTurtle.forward(100);
    myTurtle.right(90);
    myTurtle.forward(100);
    myTurtle.right(90);
    myTurtle.forward(100);
createSquare();

