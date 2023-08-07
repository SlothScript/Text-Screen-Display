class screen:
	def __init__(self, screenWH, screenHeight="", seporationChar=" ", emptyCellChar="+", newlinechar="\n", DataToScreenDict={}, screenData=None):
		try:
			self.SW = int(screenWH)
			try:
				self.SH = int(screenHeight)
			except:
				raise TypeError("screenHeight not given")
		except :
			self.SW, self.SH = screenWH
		self.DTKey = DataToScreenDict
		self.sepo = seporationChar
		self.emtSqr = emptyCellChar
		if not screenData:
			self.screenInfo = [eval(("[],"*self.SW)[0:-1])]
		else:
			self.screenInfo = screenData
		self.NLC = newlinechar
		if screenData:
			self.displayScreen()
	
	def setSData(self, data):
		self.screenInfo = data
	
	def addDType(self,DTKey):
		self.DTKey = self.DTKey | DTKey
		return self.DTKey
	
	def setDType(self,DTKey):
		self.DTKey = DTKey
	
	def changeEmptyPx(self, changeto):
		self.emtSqr = changeto
	
	def changeSepo(self, newSepo):
		self.sepo = newSepo
	
	def displayScreen(self):
		ln = []
		for y in range(self.SH):
			for x in range(self.SW):
				try:
					toprint = self.DTKey.get(self.screenInfo[y][x])
				except:
					toprint = self.emtSqr
				if toprint:
					print(toprint,end=self.sepo)
				else:
					print(self.emtSqr,end=self.sepo)
			print(self.NLC,end="")

def main():
	# An example display
	# import console
	S = screen(10,10)
	S.addDType({"player": "|"})
	# console.clear()
	S.setSData([["player"]])
	S.displayScreen()
	

if __name__ == "__main__":
	main()
