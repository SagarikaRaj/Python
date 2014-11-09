#declaring ten dictionaries with priority, list
# list contains timestamp, description
import datetime

list0 = [{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):"Get Milk"},{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):"Get Water"}]
list1 = [{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):"Wake up"}]
list2 = []
list3 = [{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):"Attend Class"},{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):"Play"},{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):"Eat"}]
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
D0 = {'0':list0}
D1 = {'1':list1}
D2 = {'2':list2}
D3 = {'3': list3}
D4 = {'4': list4}
D5 = {'5': list5}
D6 = {'6': list6}
D7 = {'7': list7}
D8 = {'8': list8}
D9 = {'9': list9}
PQ = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9 ]   #definition of priority queue

#function definition to add elements into appropriate queue
def put(p,t):
    print ("RANDOM PRIORITY SELECTED IS ",p)
    exec('list' + p + '.append({datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):t})')
    print ("ITEM ADDED TO THE QUEUE OF "+p+" PRIORITY")

#function to list all the priority queues and its contents
def list_all():
    print (str(PQ))

#function to retrieve the head element from an appropriate priority queue 
def get(p):
    if(eval('len({}{})'.format('list', str(p))) > 0):
        exec ('list%s.pop(0)' %p)
        print("in if")
    else:
        print ("DELETE FAILED ... QUEUE AT PRIORITY %s HAS NO ELEMENTS TO DELETE" %p)
  
    
#creating a random priority
import random
priorityAdd = str(random.randint(0,9))
task = "Go to Class"  # creating a task to add to the queue
put(priorityAdd,task)    # function call to add the task into the random priority queue
print ("LISTING ALL PRIORITY QUEUES AFTER INSERTION")
list_all()
priorityRemove = str(random.randint(0,9)) #creating a random priority from which the head element would be removed
print ("RANDOM PRIORITY QUEUE SELECTED FOR DELETION", priorityRemove)
get(priorityRemove) # function call to remove the first element from the appropriate priority queue
print ("LISTING ALL PRIORITY QUEUES AFTER DELETION") 
list_all() # function call to list the whole priority queue structure


