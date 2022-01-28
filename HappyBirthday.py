def happy():
	print("Happy birthday to you")
	pass

def happy_name(name):
	happy()
	happy()
	print("Happy birthday,dear {}!".format(name))
	happy()

happy_name("Paul")