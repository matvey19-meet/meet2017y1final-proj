import turtle
SIZE_X=1000
SIZE_Y=500
up_edge=250
down_edge=-250
turtle.setup(SIZE_X,SIZE_Y)

turtle.hideturtle()


turtle.penup()
SQUARE_SIZE=20
START_LENGTH=8
pos_list=[]
stamp_list=[]
log=turtle.clone()
log.shape('square')
log.color('brown')

def make_log():
    for i in range(START_LENGTH):
        x_pos=log.pos()[0]
        y_pos=log.pos()[1]
        x_pos+=SQUARE_SIZE
        my_pos=(x_pos,y_pos)
        log.goto(x_pos,y_pos)
        pos_list.append(my_pos)
        new_stamp=log.stamp()
        stamp_list.append(new_stamp)


make_log()


log1=turtle.clone()
log1.shape('square')
log1.color('brown')
log1.goto(-200,0)


def make_log1():
    for i in range(START_LENGTH):
        x_pos=log1.pos()[0]
        y_pos=log1.pos()[1]
        x_pos+=SQUARE_SIZE
        my_pos=(x_pos,y_pos)
        log1.goto(x_pos,y_pos)
        pos_list.append(my_pos)
        new_stamp=log1.stamp()
        stamp_list.append(new_stamp)

make_log1()

log2=turtle.clone()
log2.shape('square')
log2.color('brown')
log2.goto(-400,0)

def make_log2():
    for i in range(START_LENGTH):
        x_pos=log2.pos()[0]
        y_pos=log2.pos()[1]
        x_pos+=SQUARE_SIZE
        my_pos=(x_pos,y_pos)
        log2.goto(x_pos,y_pos)
        pos_list.append(my_pos)
        new_stamp=log2.stamp()
        stamp_list.append(new_stamp)
make_log2()

log3=turtle.clone()
log3.shape('square')
log3.color('brown')
log3.goto(200,0)

def make_log3():
    for i in range(START_LENGTH):
        x_pos=log3.pos()[0]
        y_pos=log3.pos()[1]
        x_pos+=SQUARE_SIZE
        my_pos=(x_pos,y_pos)
        log3.goto(x_pos,y_pos)
        pos_list.append(my_pos)
        new_stamp=log3.stamp()
        stamp_list.append(new_stamp)
make_log3()

def move_log():
    for my_pos in pos_list:
    #my_pos=log.pos()
        x_pos=my_pos[0]
        y_pos=my_pos[1]
        log.goto(x_pos,y_pos+SQUARE_SIZE)
        pos_list.append(my_pos)
        new_stamp=log.stamp()
        stamp_list.append(new_stamp)
        old_stamp=stamp_list.pop(0)
        log.clearstamp(old_stamp)
        pos_list.pop(0)
        new_pos=log.pos()
    
        

    TIME_STEP=10
    turtle.ontimer(move_log,TIME_STEP)
    

move_log()

    


