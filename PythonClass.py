class TimeTable():
	"""docstring for TimeTable"""
	def __init__(self,checi,fstation,tstation,fdate,ftime,ttime):
		self.checi=checi
		self.fstation=fstation
		self.tstation=tstation
		self.fdate=fdate
		self.ftime=ftime
		self.ttime=ttime

	def printinfo(self):
		print("车次：",self.checi)
		print("出发站：",self.fstation)
		print("到达站：",self.tstation)
		print("出发时间：",self.fdate)


a1 = TimeTable("G11","xian","beijing","2022-01-20","13:00","18:00")
a2 = TimeTable("T11","xian","beijing","2022-01-21","13:00","19:00")
a3 = TimeTable("Y11","xian","beijing","2022-01-22","13:00","20:00")

a1.printinfo()
a2.printinfo()

TimeTable.printinfo(a3)

