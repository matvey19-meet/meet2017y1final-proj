###CHARACTER###:\
import turtle

turtle.tracer(1,0)

pos_list = []

#CREATE CHARACTER SHAPE

turtle.register_shape("characterleft.gif")
turtle.register_shape("characterright.gif")
character= turtle.clone()
character.shape("characterright.gif")
character.penup()
turtle.hideturtle()

#CONSTRUCT CHARACTER

start_pos = character.pos()

UP_ARROW = "w"
LEFT_ARROW = "a"   
DOWN_ARROW = "s"
RIGHT_ARROW = "d"

TIME_STEP = 100
speed = 10

SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

num_1=3
num_2= 5


direction = UP
horizontal_direction = RIGHT

def up():
    global direction
    direction = UP
    move_char()
    #print("You pressed the up key")
    
def left():
    global direction, horizontal_direction
    direction = LEFT
    horizontal_direction = LEFT
    character.shape("characterleft.gif")
    move_char()
    #print("You pressed the left key")
    
def down():
    global direction
    direction = DOWN
    move_char()
    #print("You pressed the down key")
    
def right():
    global direction, horizontal_direction
    direction=RIGHT
    horizontal_direction = RIGHT
    character.shape("characterright.gif")
    move_char()
    #print("You pressed the right key")

turtle.hideturtle()
#______________________________________________________________________________________________|    
def jump_right():                                                                              
  
    turtle.ontimer(character.goto(character.pos()[0], character.pos()[1]),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ 2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]+ 1),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- 1),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- 2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]+num_1, character.pos()[1]- num_2),speed)

def jump_left():
  
    turtle.ontimer(character.goto(character.pos()[0], character.pos()[1]),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ 4),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ 3),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ 2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]+ 1),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- 1),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- 2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- 3),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- 4),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)
    turtle.ontimer(character.goto(character.pos()[0]-num_1, character.pos()[1]- num_2),speed)

def jump():
    if horizontal_direction==LEFT:
        return(jump_left())
    elif horizontal_direction==RIGHT:
        return(jump_right())

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













    
