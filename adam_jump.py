

###CHARACTER###:\
import turtle
SIZE_X=1000
SIZE_Y=500
up_edge=250
down_edge=-250
height=30
length=100
turtle.setup(SIZE_X,SIZE_Y)
turtle.tracer(1,0)
pos_list = []
turtle.bgpic('bg.gif')

pos_list = []
eatenfood = []
#REGISTERING SHIT


turtle.penup()
turtle.register_shape('pleasework.gif')
turtle.register_shape("characterleft.gif")
turtle.register_shape("characterright.gif")
turtle.register_shape('work.gif')
character= turtle.clone()
character.shape("characterright.gif")
character.penup()
character.goto(-450, 10)
turtle.hideturtle()


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
log.goto(100,200)
log_list.append(log)

log = turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
log.goto(-100,200)
log_list.append(log)

log=turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
log.goto(-300,200)
log_list.append(log)


log_list.reverse()
#CONSTRUCT CHARACTER

food_list=[]
for i in range (1):
    obj=turtle.clone()
    obj.showturtle()
    obj.shape('circle')
    obj.penup()
    obj.goto(-420,100)
    food_list.append(obj)


start_pos = character.pos()

UP_ARROW = "Up"
LEFT_ARROW = "Left"   
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

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
current_log = -1
on_log = False
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
    global current_log,on_log
    move_x = num_1
    move_y = [num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,2,1,-1,-2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2]
    success = False

    

    for i in move_y:
        if success != True:
            new_x = character.pos()[0] + move_x
            new_y = character.pos()[1] + i
            turtle.ontimer(character.goto(new_x,new_y),speed)
            for eaten in eatenfood:
                eaten.goto(character.pos())
            #add aya's code to check for landing
            #if land, break
            x_pos=character.pos()[0]
            y_pos=character.pos()[1]
            for log in log_list:
                log_x = log.pos()[0]
                log_y = log.pos()[1]
                if i < 13 and log_x - length <= x_pos and x_pos <= log_x + length and log_y <= y_pos and y_pos <= log_y + 10:
                    character.goto(x_pos, log_y + 20)
                    current_log = log_list.index(log)
                    on_log = True
                    success = True
                    break
            if x_pos >= 390:
                success = True
                win()
                break
        else:
            break
    if success == False:
        quit()

def jump_left():
    global current_log
    move_x = -num_1
    move_y = [num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,num_2,2,1,-1,-2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2,-num_2]
    success = False

    

    for i in move_y:
        if success != True:
            new_x = character.pos()[0] + move_x
            new_y = character.pos()[1] + i
            turtle.ontimer(character.goto(new_x,new_y),speed)       
            for eaten in eatenfood:
                eaten.goto(character.pos())
            #add aya's code to check for landing
            #if land, break
            x_pos=character.pos()[0]
            print(x_pos)
            y_pos=character.pos()[1]
            for log in log_list:
                log_x = log.pos()[0]
                log_y = log.pos()[1]
                if i>13 and log_x - length <= x_pos and x_pos <= log_x + length and log_y <= y_pos and x_pos <= log_y + 10:
                    character.goto(x_pos, log_y + 10)
                    success = True
                    on_log = True
                    current_log = log_list.index(log)
                    break
        else:
            break
    if success == False:
        quit()

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
    global current_log

    my_pos = character.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        new_pos = (x_pos + 20, y_pos)
        if on_log:
            if current_log != 3:
                log = log_list[current_log]
                if new_pos[0] >= log.pos()[0] + length:
                    character.goto(x_pos + 20, -250)
                    win()
                    quit()
                else:
                    character.goto(new_pos)
            else:
                character.goto(new_pos)
        elif new_pos[0] <= -390:
            character.goto(new_pos)
        if new_pos[0] >= 390:
            character.goto(new_pos)
            win()

    elif direction==LEFT:
        new_pos = (x_pos - 20, y_pos)
        if on_log:
            if current_log != 0:
                log = log_list[current_log]
                if new_pos[0] <= log.pos()[0] - length:
                    character.goto(x_pos - 20, -250)
                    quit()
                else:
                    character.goto(new_pos)
            else:
                character.goto(new_pos)
        if new_pos[0] <= -390:
            character.goto(new_pos)

    elif direction==UP:
        if not(on_log):
            character.goto(x_pos,y_pos + 20)
    elif direction==DOWN:
        if not(on_log):
            character.goto(x_pos, y_pos - 20)

    my_pos = character.pos()
    pos_list.append(my_pos)
    
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




def win():
    win = True
    if character.pos()[0] >= 390:
        for food in food_list:
            if food.pos()[0] < 390:
                win = False
    else:
        win = False

    if win == True:
        turtle.pencolor('white')
        turtle.goto(-350,-100)
        turtle.write( 'you won') , move=False, align="left", font=("Arial", 120, "normal"))

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
            if on_log and i == current_log:
                character.goto(character.pos()[0],log.pos()[1]+20)
                for eaten in eatenfood:
                    eaten.goto(character.pos())
        else:
            log.goto(lx,ly-SQUARE_SIZE)
            if on_log and i == current_log:
                character.goto(character.pos()[0],log.pos()[1]+20)
                for eaten in eatenfood:
                    eaten.goto(character.pos())
            
    turtle.ontimer(move_log,500)
move_log()


4
