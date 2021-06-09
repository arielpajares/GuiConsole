class Gui():
	def __init__(self,engine):
		self.engine = engine

	def Text(self,room,text,x,y):
		indexText = 0
		for i in text:
			room[y][x+indexText] = i
			indexText += 1

		return room
