from MP2b import MP2bTask
from MP2b import MP2bPriorityQUtils
import datetime

ID = 1 #id which is unique for every task object created

# Menu for user interface...
menu = """
Please enter one of the following operations: 
get
put
dump
stop
"""

# Driver code start here
while True:
	response = input(menu)
	if response == 'get':
		MP2bPriorityQUtils.get()
	elif response == 'put' :
		priorityLevel = int(input("Please enter priority level: "))
		taskDescription = input("Please enter task description: ")
		t1 = MP2bTask.Task()
		t1.set(ID,datetime.datetime.now(),taskDescription)
		#print("Task added to the PQ is :",t1.display())
		MP2bPriorityQUtils.put(priorityLevel,t1)
		ID  = ID + 1
	elif response == 'dump' : MP2bPriorityQUtils.dump()
	elif response == 'stop' : break
	else : continue
