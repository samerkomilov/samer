#bismillah
#muallif: Samer Komilov
#Dars: turtle funksiyasi bilan ishlash
#sana: 23.03.2025
from turtle import Turtle, Screen
oyna = Screen()
oyna.title("Mening o'yinim")

chiziq = Turtle()
chiziq.color('blue')
chiziq.pensize(5)
chiziq()
chiziq.hideturtle()
chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)

koptok = Turtle()
koptok.shape('circle')
koptok.color('red')
koptok.up()
koptok.goto(0, 0)

step_x = 3
step_y = 2 
while True:
    x, y = koptok.position()
    
    if x + step_x >= 300 or x + step_x <= -300:
        step_x = -step_x
    if y + step_y >= 300 or y + step_y <= -300:
        step_y = -step_y
        
    koptok.goto(x+step_x, y+step_y)
    
oyna.mainloop() 



