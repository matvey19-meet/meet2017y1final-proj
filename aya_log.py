
import turtle
SIZE_X=1000
SIZE_Y=500
up_edge=250
down_edge=-250
height=20
length=80
turtle.setup(SIZE_X,SIZE_Y)
turtle.bgpic('bg.gif')

turtle.hideturtle()
turtle.register_shape('pleasework.gif')
turtle.register_shape('burger.gif')
food=turtle.clone()
food.shape('burger.gif')
food.showturtle()
food.goto(-400,0)


turtle.penup()

turtle.goto(300,0)
log_list = []

log=turtle.clone()
log.showturtle()
log.shape('pleasework.gif')
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

##(x,y)=log.pos()
##def land():
##    success = False
##    x_pos=character.pos()[0]
##    y_pos=character.pos()[1]
##    for log in log_list:
##        log_top=log.pos()[1]+height
##        log_x=log.pos()[0]
##        if(y_pos<=log_top+5) and (y_pos>=log_top-5) and (x_pos>=log_x-length) and(x_pos<=log_x+length):
##            character.goto(x_pos, log_top)
##            success = True
##            break
##    if success == False:
##        quit()
##            
