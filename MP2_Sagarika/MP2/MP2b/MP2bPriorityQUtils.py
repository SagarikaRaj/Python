from MP2b import MP2bTask

MAX_PRIORITY = 10

# Configure the Priority Queue with a List with priority level as index
PQ = [ [], [], [], [], [], [], [], [], [], [] ]

#get() function to retrieve the head element of every priority and pop it out
def get():
    for i in range(MAX_PRIORITY):
        if not PQ[i] == []:
            t1 = MP2bTask.Task()
            t1 = PQ[i][0].get()
            print('Element at priority level: ' , i, ' has been processed!')
            print(t1.display())
            PQ[i][0] = []

#method to add an item to the PQ at the right priority
def put(priority, D):
    PQ[priority].append(D)
    print("Element added at priority ", priority)

#method to display the PQ contents
def dump():
    print ("\n PQ Current Contents:")
    t1 = MP2bTask.Task()
    for i in range(MAX_PRIORITY):
        if not PQ[i] == []:
            count = len(PQ[i])
            print("Tasks At priority :", i)
            for j in range(count):
                if not PQ[i][j] == []:
                    t1 = PQ[i][j].get()
                    t1.display()