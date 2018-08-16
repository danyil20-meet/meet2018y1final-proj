import turtle
import random
import random

turtle.tracer(1,0)

poacher = turtle.Turtle()
tree = turtle.Turtle()
'''
turtle.register_shape("tree.gif")
turtle.register_shape('poacher.gif')

poacher.shape('poacher.gif')
tree.shape('tree.gif')
'''
border = turtle.clone()
border.penup()
border.goto(300,300)
border.pendown()
border.goto(300, -300)
border.goto(-300,-300)
border.goto(-300, 300)
border.goto(300,300)
border.hideturtle()

score = 0

STEP = 20

direction = None

#TIME_STEP =

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

poacher_pos = None
tree_pos_list = []

def W():
    global direction
    global poacher
    global poacher_pos
    direction = UP
    poacher_pos = poacher.pos()
    #move_poacher
    print("You pressed W")

def S():
    global direction
    global poacher
    global poacher_pos
    direction = DOWN
    poacher_pos = poacher.pos()
    #move_poacher
    print("You pressed S")

def A():
    global direction
    global poacher
    global poacher_pos
    direction = LEFT
    poacher_pos = poacher.pos()
    #move_poacher
    print("You pressed A")

def D():
    global direction
    global poacher
    global poacher_pos
    direction = RIGHT
    poacher_pos = poacher.pos()
    #move_poacher
    print("You pressed D")

turtle.onkeypress(W , "Up")
turtle.onkeypress(S , "Down")
turtle.onkeypress(A , "Left")
turtle.onkeypress(D , "Right")

turtle.listen()

def move_poacher():
    global poacher_pos
    
    poacher_pos = poacher.pos()
    x_pos = poacher_pos[0]
    y_pos = poacher_pos[1]

    if direction==RIGHT:
        poacher.goto(x_pos + STEP, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        poacher.goto(x_pos - STEP, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        poacher.goto(x_pos, y_pos - STEP)
        print('You moved down!')
    elif direction==UP:
        poacher.goto(x_pos, y_pos+ STEP)
        print('You moved up!')

    new_poacher_pos = poacher.pos()
    new_x_pos = poacher_pos[0]
    new_y_pos = poacher_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()
    turtle.ontimer(move_poacher, 200)

move_poacher()
    
