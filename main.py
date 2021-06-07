import os
import time
import keyboard


class Engine():
	def __init__(self):
		pass

	def FillRoom(self,width,height,Fill):
		room = []
		for i in range(height):
			fillroom = []
			for j in range(width):
				fillroom.append(Fill)
			room.append(fillroom)

		return room

	def PrintRoom(self,room):
		for i in room:
			printroom = ""
			for j in i:
				printroom += j

			print(printroom)

class Gui():
	def __init__(self,room):
		pass

# Variables.

KeybordInput = keyboard.read_key()
engine = Engine()
room = engine.FillRoom(50,25,"X")
engine.PrintRoom(room)

