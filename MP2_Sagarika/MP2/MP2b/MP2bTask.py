# Class definition of Task with variables id, currentTimeStamp and description
# and methods to set, get and display
class Task:

	def set(self,task_id,currentTimeStamp,description):
		self.task_id = task_id
		self.currentTimeStamp= currentTimeStamp
		self.description = description
	
	def get(self):
		return self
	
	def display(self):
		print("Task id = ",self.task_id, "Task timestamp = ", self.currentTimeStamp , "Task Description = ", self.description)
	
	