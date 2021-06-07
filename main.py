import os
import time
import keyboard

# Variables.

KeybordInput = keyboard.read_key()

class Engine():
	def __init__(self):
		self.room = []
		self.width = 50
		self.height = 25

	def FillRoom(self):
		for i in range(self.height):
			fillroom = []
			for j in range(self.width):
				fillroom.append(" ")
			self.room.append(fillroom) 

	def PrintRoom(self):
		for i in range(self.height):
			for j in range(self.width):
				print(self.room[i][j])

class Gui():
	def __init__(self):
		 