import turtle
SIZE_X=1000
SIZE_Y=500
up_edge=250
down_edge=-250
turtle.setup(SIZE_X,SIZE_Y)

turtle.hideturtle()
turtle.bgpic('bg.gif')

turtle.penup()
SQUARE_SIZE=20
START_LENGTH=8
pos_list=[]
stamp_list=[]
log=turtle.clone()
log.shape('pleasework')

def make_log(x,y):
    x_pos=x
    y_pos=y
    for i in range(START_LENGTH):
        my_pos=(x_pos,y_pos)
        pos_list.append(my_pos)
        x_pos+=SQUARE_SIZE
        #my_pos=(x_pos,y_pos)
        log.goto(x_pos,y_pos)
        #pos_list.append(my_pos)
        new_stamp=log.stamp()
        stamp_list.append(new_stamp)


make_log(200,0)
make_log(0,0)
make_log(-200,0)
make_log(-400,0)
##
##pos_list2 = pos_list[:]
##
##def move_log():
##    for my_pos in pos_list2:
##        #my_pos=log.pos()
##        x_pos=my_pos[0]
##        y_pos=my_pos[1]
##        log.goto(x_pos,y_pos+SQUARE_SIZE)
##        my_pos=log.pos()
##        #pos_list.append(my_pos)
##        
##        
##        old_stamp=stamp_list.pop(0)
##        log.clearstamp(old_stamp)
##        new_stamp=log.stamp()
##        stamp_list.append(new_stamp)
##        pos_list.pop(0)
##    
##        
##
##TIME_STEP=10
##turtle.ontimer(move_log,TIME_STEP)
##    
##
##move_log()

    


