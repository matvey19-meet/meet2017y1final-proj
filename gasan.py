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
###########################3
#aya's code
pos_list = []
turtle.bgpic('bg.gif')
#REGISTERING SHIT
######################3#####

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
turtle.goto(300,0)
log_list = []

log=turtle.clone()
log.showturtle()
log.shape("pleasework.gif")
log_list.append(log)

log=turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
log.goto(100,0)
log_list.append(log)

log = turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
log.goto(-100,0)
log_list.append(log)

log=turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
log.goto(-300,0)
log_list.append(log)


############################

#Gasan's code
food_list=[]
for i in range (1):
    obj=turtle.clone()
    obj.showturtle()
    obj.shape('triangle')
    obj.penup()
    obj.goto(-420,100)
    food_list.append(obj)


############################
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
                        character.goto(x_pos, log_top)
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
                        character.goto(x_pos, log_top)
                        
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
eatenfood=[]
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

################################
#win condition
def win():
    win = True
    if character.pos()[0] >= 390:
        for food in food_list:
            if food.pos()[0] < 390:
                win = False
    else:
        win = False

    if win = True:
        print('You win!!!!!!!')

###############################################
#Gasan's code
    for i in range (len(food_list)):
        nutrition=food_list[i]
        cx = character.pos()[0]
        cy = character.pos()[1]
        fx = nutrition.pos()[0]
        fy = nutrition.pos()[1]

        d = ((fx-cx)**2 + (cy-fy)**2)**0.5
        if d <= 20:
            eatenfood.append(nutrition)

    for eaten in eatenfood:
        eaten.goto(character.pos())
#################################################









    
