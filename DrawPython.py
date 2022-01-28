#e2.1DrawPython.py
import turtle	
turtle.setup(650,350,200,200)	#设置画布
turtle.penup()					#抬起画笔
turtle.fd(-250)					
turtle.pendown()				#落下画笔
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)				#改变角度
for i in range(4):
	turtle.circle(40,80)
	turtle.circle(-40,80)
	pass
turtle.circle(40.80/2)
turtle.fd(40)					#forward 前进
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()