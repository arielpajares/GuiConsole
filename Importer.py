import os

class OpenFiles():
	def __init__(self):
		pass

	def OpenFile(directory):
		file = open(directory,"r")
		FileContent = file.read()
		file.close()

		return FileContent