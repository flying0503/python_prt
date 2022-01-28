#pr1.3 Drawsqr
import turtle

def DrawSetup():
	turtle.setup(1024,720,200,200)	#设置画布
	turtle.speed(1)
	turtle.color("blue")
	pass

def Drawsqr(lenth):
	turtle.pendown()
	turtle.forward(lenth)
	turtle.left(90)
	turtle.forward(lenth)
	turtle.left(90)
	turtle.forward(lenth+10)
	return lenth+10
	pass

DrawSetup()
lenth = 10
for i in range(20):
	lenth = Drawsqr(lenth)
	pass