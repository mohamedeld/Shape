import turtle
def draw_square(square):
    for x in range(4):
        square.forward(150)
        square.right(90)
    
def move_square():
    window = turtle.Screen()
    window.bgcolor("#58acfa")

    creature = turtle.Turtle()
    creature.shape("turtle")
    creature.color("blue")
    creature.pensize(2)
    creature.speed(30)
    creature.shapesize(1)

    for i in range(80):
        draw_square(creature)
        creature.right(5)
    window.exitonclick()
move_square()