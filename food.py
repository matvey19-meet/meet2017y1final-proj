import turtle
import random
turtle.penup()

food = turtle.clone()
food.shape('circle')


SQUARE_SIZE=20
square_length =1
SIZE_X=800
SIZE_Y=500
food_pos =[]
food_stamps=[]
stamp_list=[]
turtle.setup(SIZE_X,SIZE_Y)
start_width=100

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=-int(SIZE_X/4/SQUARE_SIZE)
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    new_pos=(food_x,food_y)
    food_pos.append(new_pos)
    stamp_id=food.stamp()
    food_stamps.append(stamp_id)

    
    
food.hideturtle()
make_food()
food.showturtle()
new_character=my_character.append(food_stamp)


for i in range (1):
    obj=turtle.clone()
    obj,shape('circle')
    obj.penup()
    obj.goto(-300,100)
    food_list.append(obj)

eaten.food=[]
for i in range (1)
food=food_list[i]
if character.pos()=food.pos():
    eatinfood.append(i)
    


