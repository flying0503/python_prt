PM = eval(input("请输入 PM2.5数值:"))
if 0 <=PM<35:
	print("空气质量优")
if 35<=PM<75:
	print("空气质量良")
if 75<=PM:
	print("空气质量差")