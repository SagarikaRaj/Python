import Task
from tkinter import *


MAX_PRIORITY = 10

# Configure the Priority Queue with a List with priority level as index
PQ = [ [], [], [], [], [], [], [], [], [], [] ]
taskList = [Task.Task(),Task.Task(),Task.Task(),Task.Task(),Task.Task(),Task.Task(),Task.Task(),Task.Task(),Task.Task()]

#get() function to retrieve the head element of every priority and pop it out
def get():
    for i in range(MAX_PRIORITY):
        
        if not PQ[i] == []:
            taskObject = Task.Task()
            flag = 1
            print("Element at priority level: " + str(i) + " has been processed!")
            taskObject = PQ[i].pop()
            print(taskObject.description)
            taskList[i] = taskObject
        else:
            flag = 0
    if (flag == 0):    
        print("Priority Queue Empty")
    return taskList
   

#method to add an item to the PQ at the right priority
def put(priority, D):
    PQ[priority].append(D)
        

#method to display the PQ contents
def dump():
    taskList = [ [], [], [], [], [], [], [], [], [], [] ]
    for i in range(MAX_PRIORITY):
        if not PQ[i] == []:
            count = len(PQ[i])
            for j in range(count):
                if not PQ[i][j] == []:
                    taskObject = PQ[i][j].get()
                    taskList[i].append(taskObject)
    return taskList