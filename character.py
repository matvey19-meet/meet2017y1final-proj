###CHARACTER###:\
import turtle

turtle.tracer(1,0)

pos_list = []

#CREATE CHARACTER SHAPE

turtle.register_shape("character.gif")
character= turtle.clone()
character.shape("character.gif")
turtle.hideturtle()

#CONSTRUCT CHARACTER

start_pos = character.pos()

UP_ARROW = "Up"
LEFT_ARROW = "Left"   
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

TIME_STEP = 100
speed = 50

SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


direction = UP
horizontal_direction = RIGHT

def up():
    global direction
    direction = UP
    move_char()
    print("You pressed the up key")
    
def left():
    global direction, horizontal_direction
    direction = LEFT
    horizontal_direction = LEFT
    move_char()
    print("You pressed the left key")

def down():
    global direction
    direction = DOWN
    move_char()
    print("You pressed the down key")

def right():
    global direction, horizontal_direction
    direction=RIGHT
    horizontal_direction = RIGHT
    move_char()
    print("You pressed the right key")

    
def jump():
  
    turtle.ontimer(character.goto(character.pos()[0], character.pos()[1]),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]+ 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)
    turtle.ontimer(character.goto(character.pos()[0]+10, character.pos()[1]- 10),speed)



turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(jump, SPACEBAR)

turtle.listen()

def move_char():

    my_pos = character.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        character.goto(x_pos + 20, y_pos)

    elif direction==LEFT:
        character.goto(x_pos - 20, y_pos)

    elif direction==UP:
        character.goto(x_pos,y_pos + 20)
    elif direction==DOWN:
        character.goto(x_pos, y_pos - 20)

    my_pos = character.pos()
    pos_list.append(my_pos)













    
