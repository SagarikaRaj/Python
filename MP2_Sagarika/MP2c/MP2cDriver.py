from Queue import PriorityQueue
import MP2cTask
import datetime

# Menu for user interface...
menu = """
Please enter one of the following operations: 
get
put
dump
stop
"""
pq = PriorityQueue() #define priority queue pq


# Driver code start here
while True:
    response = raw_input(menu)
    if response == 'get':
        test = pq.get() #get the first element from the pq
        testobj = MP2cTask.Task()
        testobj = test[1]
        print ("QUEUE ITEM PROCESSED IS :", test[0], "AND THE OBJECT IS", testobj.display())
        
    elif response == 'put' :
        priorityLevel = int(raw_input("PLEASE ENTER PRIORITY LEVEL: "))
        taskDescription = raw_input("PLEASE ENTER TASK DESCRIPTION: ")
        t1 = MP2cTask.Task()
        t1.set(datetime.datetime.now(),taskDescription)
        print "ELEMENT ADDED AT PRIORITY ", priorityLevel
        pq.put((priorityLevel,t1)) # priority queue of structure (priority,task)
        
    elif response == 'dump' :  #display function for list_all
        for pcb in pq.queue:
            test = pcb
            testobj = MP2cTask.Task()
            testobj = test[1]
            print "PRIORITY",test[0],"TASK OBJECT" ,testobj.display() #display the retrieved pq
            
    elif response == 'stop' : break
    else : continue


