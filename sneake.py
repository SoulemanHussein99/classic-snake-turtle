import turtle as sn
import random as r
import time

sn.Screen()
sn.setup(width=600,height=600)
sn.hideturtle()
sn.bgcolor("purple")
sn.penup()
sn.tracer(0)



highest_scoore =0
scoore =0
color = ["white", "orange", "yellow", "green"]
food = ["circle", "square"]
ok1 = "w"
ok2 = "s"
ok3 = "a"
ok4 = "d" 
i = 0
delay = 0.1


x = r.randint(-270,270)
y = r.randint(-270,270)
size = 1.0
# sneake 
s = sn.Turtle()
s.penup()
s.color("black")
s.shape("square")
s.shapesize(1,size)
s.setposition(0,0)
s.diraction = "stop"

# food 
f = sn.Turtle()
f.penup()
f.speed(0)
f.color(r.choice(color))
f.shape(r.choice(food))
f.shapesize(0.8)
f.setposition(x,y)

#scoore 
sc = sn.Turtle()
sc.penup()
sc.hideturtle()
sc.speed(0)
sc.color("white")
sc.setposition(0,280)
sc.write("scoore : "+str(scoore)+"  |    highest scoore : "+str(highest_scoore),align="center", font=("Arial", 14 , "normal"))



# move
def move():
    if s.diraction == "up":
        y1 = s.ycor()
        s.sety(y1 + 20)
    if s.diraction == "down":
        y1 = s.ycor()
        s.sety(y1 - 20)
    if s.diraction == "left":
        x1 = s.xcor()
        s.setx(x1 - 20)
    if s.diraction == "right":
        x1 = s.xcor()
        s.setx(x1 + 20)

def up():
    if s.diraction != "down":
        s.diraction = "up"
        s.setheading(90)
    
    
def down():
    if s.diraction != "up":
        s.diraction = "down"
        s.setheading(270)
    
def left():
    if s.diraction != "right":
        s.diraction = "left"
        s.setheading(180)
def right():
    if s.diraction != "left":
        s.diraction = "right"
        s.setheading(0)
    
segment = []

sn.onkeypress(up,ok1)
sn.onkeypress(down,ok2)
sn.onkeypress(left,ok3)
sn.onkeypress(right,ok4)
sn.listen()

while True: 
    sn.update()
    color = ["white", "orange", "yellow", "green"]
    food = ["circle", "square"]
    x = r.randint(-270,270)
    y = r.randint(-270,270)
    # food eating
    if s.distance(f) < 20:
        f.color(r.choice(color))
        f.shape(r.choice(food))
        f.setposition(x,y)
        s2 = sn.Turtle()
        s2.color("gray")
        s2.shape("square")
        s2.shapesize(0.8)
        s2.penup()
        s2.speed(0)
        segment.append(s2)
        scoore +=1
        sc.clear()
        sc.write("scoore : "+str(scoore)+"  |    highest scoore : "+str(highest_scoore),align="center", font=("Arial", 14 , "normal"))
    # creating the body    
    for i in range(len(segment) - 1,0,-1):
            x1=segment[i-1].xcor()
            y1=segment[i-1].ycor()
            segment[i].goto(x1,y1)
    # moving behind the head
    if len(segment) > 0:
            x1 = s.xcor()
            y1 = s.ycor()
            segment[0].goto(x1,y1)
    # border hit
    if s.xcor()>290 or s.xcor()< -290 or s.ycor()> 290 or s.ycor()< -290:
        # scoore
        if highest_scoore < scoore:
            highest_scoore =scoore
            scoore = 0
            sc.clear()
            sc.write("scoore : "+str(scoore)+"  |    highest scoore : "+str(highest_scoore),align="center", font=("Arial", 14 , "normal"))
        else:
            scoore = 0
            sc.clear()
            sc.write("scoore : "+str(scoore)+"  |    highest scoore : "+str(highest_scoore),align="center", font=("Arial", 14 , "normal"))
        for seg in segment:
            seg.goto(1000,1000)
        segment.clear()
        scoore = 0
        s.goto(0,0)
        s.diraction = "stop"
        
    move()
    # body hit
    for seg in segment:
        if seg.distance(s) < 20:
            s.diraction = "stop"
            # scoore
            if highest_scoore < scoore:
                    highest_scoore =scoore
                    scoore = 0
                    sc.clear()
                    sc.write("scoore : "+str(scoore)+"  |    highest scoore : "+str(highest_scoore),align="center", font=("Arial", 14 , "normal"))
            else:
                    scoore = 0
                    sc.clear()
                    sc.write("scoore : "+str(scoore)+"  |    highest scoore : "+str(highest_scoore),align="center", font=("Arial", 14 , "normal"))
            for seg in segment:
                    seg.goto(1000,1000)
            segment.clear()
            scoore = 0
            s.goto(0,0)
            
            
        
    
        
        
        
       
        
    
    
      

    time.sleep(delay)
    
    
    
                  
    
       