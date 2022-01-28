#pr1.2 DrawTryang2
import turtle

def DrawSetup():
	turtle.setup(1024,720,200,200)	#设置画布
	turtle.speed(1)
	turtle.color("blue")
	pass	

def DrawTryang(x,y):
	turtle.penup()					#抬起画笔
	turtle.seth(0)
	turtle.goto(x,y)
	turtle.pendown()
	turtle.fd(200)
	turtle.left(60*2)
	turtle.fd(200)
	turtle.left(60*2)
	turtle.fd(200)				
	pass

DrawSetup()
DrawTryang(-100,-50)
DrawTryang(-100-100,-173-50)
DrawTryang(100-100,-173-50)
turtle.done()

