# Class definition of Task with variables id, currentTimeStamp and description
# and methods to set, get and display


from tkinter import *
from datetime import  *

class Task:
	def __init__(self):
		self.currentTimeStamp = datetime.now()
		self.description = "dummy"
	def set(self,currentTimeStamp,description):
		self.currentTimeStamp = currentTimeStamp
		self.description = description
	def get(self):
		return self
	
