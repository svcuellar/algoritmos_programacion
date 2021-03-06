import turtle 
turtle.speed(10)
turtle.pensize(10)

def curveMove():
  for i in range(200):
    turtle.rt(1)
    turtle.fd(1)

def drawHeart():
  turtle.hideturtle()
  turtle.color("red")
  turtle.begin_fill()
  turtle.lt(120)
  turtle.fd(111.65)
  curveMove()
  turtle.lt(120)
  curveMove()
  turtle.fd(111.65)
  turtle.end_fill()
  
if __name__ == '__main__':
  drawHeart()

t=turtle.Turtle()
t.speed(3)
t.shape("circle")
t.color("pink")
t.pensize(35)
t.penup()
t.goto(-580,50)
t.pendown()
t.rt(65)
t.fd(150)
t.rt(-130)
t.fd(150)

t.color("pink")
t.penup()
t.goto(-295,50)
t.pendown()
t.lt(205)
t.fd(140)
t.lt(90)
t.fd(90)

t.color("pink")
t.penup()
t.goto(-30,-90)
t.pendown()
t.lt(90)
t.fd(140)
t.rt(145)
t.fd(170)
t.lt(145)
t.fd(140)

t.color("pink")
t.penup()
t.goto(250,50)
t.pendown()
t.bk(140)

t.color("pink")
t.penup()
t.goto(450,-90)
t.pendown()
t.rt(25)
t.fd(150)
t.rt(130)
t.fd(150)
t.penup()
t.lt(160)
t.fd(40)
t.lt(85)
t.fd(15)
t.pendown()
t.fd(90)

t.color("purple")
t.penup()
t.goto(-465,-90)
t.pendown()
t.rt(115)
t.fd(150)
t.rt(130)
t.fd(150)
t.penup()
t.lt(160)
t.fd(40)
t.lt(85)
t.fd(15)
t.pendown()
t.fd(90)

t.color("purple")
t.penup()
t.goto(-165,50)
t.pendown()
t.bk(90)
t.penup()
t.fd(90)
t.pendown()
t.lt(90)
t.fd(65)
t.lt(90)
t.fd(80)
t.bk(80)
t.rt(90)
t.fd(75)
t.lt(90)
t.fd(90)

t.color("purple")
t.penup()
t.goto(110,50)
t.pendown()
t.fd(90)
t.bk(45)
t.rt(90)
t.fd(140)

t.color("purple")
t.penup()
t.goto(305,-90)
t.lt(180)
t.pendown()
t.fd(140)
t.rt(145)
t.fd(170)
t.lt(145)
t.fd(140)