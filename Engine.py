class Engine():
	def __init__(self):
		pass

	def FillRoom(self,width,height,fill):
		room = []
		for i in range(height):
			fillroom = []
			for j in range(width):
				fillroom.append(fill)
			room.append(fillroom)

		return room

	def PrintRoom(self,room):
		for i in room:
			printroom = ""
			for j in i:
				printroom += j

			print(printroom)
