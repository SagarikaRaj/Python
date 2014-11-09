# Class definition of Task with variables id, currentTimeStamp and description
# and methods to set, get and display
class Task:

	def set(self,currentTimeStamp,description):
		self.currentTimeStamp= currentTimeStamp
		self.description = description
	
	#def get(self):
		#return self
	
	def display(self):
		print "(Task timestamp = ", self.currentTimeStamp , "Task Description = ", self.description, ")"
	
	