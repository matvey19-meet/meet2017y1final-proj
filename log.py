import turtle
SIZE_X=1000
SIZE_Y=500
up_edge=250
down_edge=-250
stamp_list=[]
log_lispos=[]
height=20
length=80
turtle.setup(SIZE_X,SIZE_Y)

turtle.hideturtle()
turtle.register_shape('pleasework.gif')


turtle.penup()

turtle.goto(300,0)
log=turtle.clone()
log.shape('pleasework.gif')
newstamp=log.stamp()
stamp_list.append(newstamp)

log.goto(100,0)
newstamp1=log.stamp()
stamp_list.append(newstamp1)
log.goto(-100,0)
stamp2=log.stamp()
stamp_list.append(stamp2)
log.goto(-300,0)
stamp3=log.stamp()
stamp_list.append(stamp3)

(x,y)=log.pos()
def land():
    x_pos=character.pos()[0]
    y_pos=character.pos()[1]
    log_top=log.pos()[1]+height
    log_x=log.pos()[0]
    if(y_pos<=log_top+5) and (y_pos>=log_top-5) and (x_pos>=log_x-length) and(x_pos<=log_x+length):
        character.goto(x_pos, log_top)
        break


    


