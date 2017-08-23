###CHARACTER###:\
import turtle
SIZE_X=1000
SIZE_Y=500
up_edge=250
down_edge=-250
height=20
length=80
turtle.setup(SIZE_X,SIZE_Y)
turtle.tracer(1,0)

pos_list = []


#REGISTERING SHIT


turtle.penup()
turtle.register_shape('pleasework.gif')
turtle.register_shape("characterleft.gif")
turtle.register_shape("characterright.gif")
character= turtle.clone()
character.shape("characterright.gif")
character.penup()
character.goto(-450, 10)
turtle.hideturtle()



##character.goto(-350,0)

#NEW CODE BEWARE!!!
turtle.goto(300,200)
log_list = []

log=turtle.clone()
log.showturtle()
log.shape("pleasework.gif")
log_list.append(log)


log=turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
log.goto(100,160)
log_list.append(log)

log = turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
log.goto(-100,120)
log_list.append(log)

log=turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
log.goto(-300,80)
log_list.append(log)



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
SPACE = 4
num_1=3
num_2= 5


direction = UP
horizontal_direction = RIGHT
log_top=log.pos()[1]+height

def up():
    global direction
    if not character.pos()[1] == log_top :
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
    if not character.pos()[1] == log_top:
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

def space():
    global direction
    direction = SPACE
    

turtle.hideturtle()
#______________________________________________________________________________________________|    
def jump_right():
    move_x = num_1
    move_y = [num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,2,1,-1,-2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2]
    success = False

    

    for i in move_y:
        if success != True:
            new_x = character.pos()[0] + move_x
            new_y = character.pos()[1] + i
            turtle.ontimer(character.goto(new_x,new_y),speed)       
            #add aya's code to check for landing
            #if land, break
            x_pos=character.pos()[0]
            print(x_pos)
            y_pos=character.pos()[1]

            if y_pos < log_top - 20:
                quit()
            elif y_pos == log_top - 10:
                for log in log_list:
                    log_x = log.pos()[0]
                    if log_x - length <= x_pos <= log_x + length:
                        character.goto(x_pos, log_top + 10)
                        success = True
                        print(success)
                        break
        else:
            break


def jump_left():
    move_x = -num_1
    move_y = [num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,2,1,-1,-2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2]
    success = False

    

    for i in move_y:
        if success != True:
            new_x = character.pos()[0] + move_x
            new_y = character.pos()[1] + i
            turtle.ontimer(character.goto(new_x,new_y),speed)       
            #add aya's code to check for landing
            #if land, break
            x_pos=character.pos()[0]
            print(x_pos)
            y_pos=character.pos()[1]

            if y_pos < log_top - 20:
                quit()
            elif y_pos == log_top - 10:
                for log in log_list:
                    log_x = log.pos()[0]
                    if log_x - length <= x_pos <= log_x + length:
                        character.goto(x_pos, log_top + 10)
                        success = True
                        print(success)
                        break
        else:
            break


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
    elif direction==SPACE:
        jump()
        direction == RIGHT
    my_pos = character.pos()
    pos_list.append(my_pos)


l_up=0
l_down=1
log_direction= [l_up,l_up,l_up,l_up]
SQUARE_SIZE=20
def move_log():
    global log_direction
    for i in range(len(log_list)):
        log = log_list[i]
        lx=log.pos()[0]
        ly=log.pos()[1]
        if ly >= SIZE_Y/2-50:
            log_direction[i]=l_down
        elif ly<=-SIZE_Y/2+50:
            log_direction[i]=l_up

        if log_direction[i]==l_up:
            log.goto(lx,ly+SQUARE_SIZE)
        else:
            log.goto(lx,ly-SQUARE_SIZE)
            
    turtle.ontimer(move_log,500)
move_log()









    
