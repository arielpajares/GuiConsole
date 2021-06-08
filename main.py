import os
import time
import keyboard


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

class Gui():
	def __init__(self,engine):
		self.engine = engine

	def Text(self,room,text,x,y):
		indexText = 0
		for i in text:
			room[y][x+indexText] = i
			indexText += 1

		return room


# Variables.

engine = Engine()
gui = Gui(engine)
room = engine.FillRoom(50,25," ")
room = gui.Text(room,"1) Hello",1,1)
room = gui.Text(room,"2) Welcome",1,2)
room = gui.Text(room,"3) Goodbye",1,3)
KeepRunning	= True
arrowPosition = 1

while KeepRunning:
	engine.PrintRoom(room)
	KeybordInput = keyboard.read_key()
	if KeybordInput	== "esc":KeepRunning = False;
	if KeybordInput == "up":
		arrowPosition -= 1
		if arrowPosition < 1:
			room = gui.Text(room," ",0,1)
			arrowPosition = 3
		room = gui.Text(room,">",0,arrowPosition)
		room = gui.Text(room," ",0,arrowPosition+1)
	if KeybordInput == "down":
		arrowPosition += 1
		if arrowPosition > 3:
			room = gui.Text(room," ",0,3)
			arrowPosition = 1
		room = gui.Text(room,">",0,arrowPosition)
		room = gui.Text(room," ",0,arrowPosition-1)
	os.system("cls")
