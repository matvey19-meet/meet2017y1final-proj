import turtle

turtle.pu()

score_list=[]


turtle.hideturtle()
    

global score
score=0
turtle.clear()
score= score + 1
score_list.append(score)
turtle.goto(-400/2+17, 250/2-18)
turtle.write('score = 0', move=True, align="right", font=("Minecrafter.Reg", 16, "normal")) 
