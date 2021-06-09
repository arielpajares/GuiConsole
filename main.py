import os
import time
import keyboard
from Engine import Engine
from Gui import Gui

# Variables.

def main():
	engine = Engine()
	gui = Gui(Engine())
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

if __name__ == "__main__":
	main()