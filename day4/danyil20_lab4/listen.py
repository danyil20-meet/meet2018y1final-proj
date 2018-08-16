
import turtle

screen = turtle.Screen()


image = "rock.gif"

screen.register_shape(image)
turtle.shape(image)

screen.bgcolor("lightblue")

move_speed = 10
turn_speed = 10


def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.home()


screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
turtle.mainLoop()
