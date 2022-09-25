import turtle
import random
import math
import time
import pickle
s = turtle.getscreen()
s.title("conveyor belt mania")
s.bgcolor("#57001b")
t = turtle.Turtle()
t.fillcolor("gray")
u = turtle.Turtle()
u.shape("square")
t.speed(100)
u.speed(100)
v = turtle.Turtle()
scoreboard = turtle.Turtle()
hi = turtle.Turtle()
hi.up()
hi.goto(0,250)
hi.down()
hi.speed(1000)
try:
    with open("hi_score.bin","rb") as hi_scoree:
        hi_score=pickle.load(hi_scoree)
        hi.write(hi_score,font=("arial",50,"bold"))
except:
    pass
scoreboard.up()
scoreboard.goto(0,300)
scoreboard.down()
scoreboard.speed(1000)
lose = False
global lol
lol=0
global mol
mol = ["black","red","blue","purple","#c99402"]
def re(b,c):
    t.up()
    t.left(90)
    t.fd(c)
    t.right(90)
    t.down()
    for i in range(2):
        t.begin_fill()
        t.fd(b)
        t.right(90)
        t.fd(c)
        t.right(90)
        t.end_fill()
    t.up()
    t.left(90)
    t.bk(c/2)
    t.right(90)
    t.fd(b/2)
t.goto(-400,-50)
re(800,100)
lis=[-100,100]
u.up()

score = 0
u.goto(random.randint(-370,370),random.choice(lis))
def space():
    t.speed(100)
    t.left(180)
    t.speed(score/20+1)
def up():
    t.sety(100)
    if t.distance(u)<20:
        u.goto(random.randint(-370,370),random.choice(lis))
        global lol
        global mol
        global score
        score+=int(lol+1)
        scoreboard.clear()
        scoreboard.write(score,font=("arial",50,"bold"))
        t.sety(0)
        lol=random.randint(0,4)
        u.fillcolor(mol[lol])
    else:
        t.clear()
        u.hideturtle()
        t.down()
        t.write("You lose",font=("arial",50,"bold"))
        t.up()
        t.hideturtle()
        lose = True
def down():
    t.sety(-100)
    if t.distance(u)<20:
        u.goto(random.randint(-380,380),random.choice(lis))
        global score
        global lol
        global mol
        score+=int(lol+1)
        scoreboard.clear()
        scoreboard.write(score,font=("arial",50,"bold"))
        t.sety(0)
        lol=random.randint(0,4)
        u.fillcolor(mol[lol])
    else:
        t.clear()
        u.hideturtle()
        t.down()
        t.write("You lose",font=("arial",50,"bold"))
        t.up()
        t.hideturtle()
        lose = True

s.onkey(up,"w")
s.onkey(down,"s")
s.onkey(space,"space")
s.listen()
t.speed(score/50+1)
while lose==False:
    s.update()
    t.fd(30)
    if t.distance(v)>399:
        t.clear()
        u.hideturtle()
        t.down()
        t.write("You lose",font=("arial",50,"bold"))
        t.up()
        t.hideturtle()
        lose = True
try:
    if score>hi_score:
        with open("hi_score.bin","wb") as new_hi:
            pickle.dump(score,new_hi)
except:
    with open("hi_score.bin","wb") as new_hi:
        pickle.dump(score,new_hi)
