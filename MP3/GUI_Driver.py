from tkinter import *
from tkinter import ttk
import datetime
import PriorityQUtils
import Task

#function to insert into the Priority Queue
def put(*args):
    try:
        priorityValue = int(priority.get())
        priorityDescValue = str(priorityDesc.get())
        t1 = Task.Task()   
        t1.set(datetime.datetime.now(),str(priorityDescValue))
        PriorityQUtils.put(int(priorityValue),t1)
        text.insert(CURRENT,"INSERT SUCCESSFUL \n")
    except ValueError:
        pass

#function to retrieve from the priority queue
def get(*args):
    text.delete("1.0", END)
    t1 =  PriorityQUtils.get()
    text.insert(CURRENT,"\nRetrieving the last element at all priorities\n")
   
    for i in range(len(t1)):
        task = t1[i].get()
        if(t1[i].description != "dummy"):
            print(task.description)
            text.insert(CURRENT,str(t1[i].currentTimeStamp) + "\t" + str(t1[i].description) + "\n\n")
            t1[i].description = "dummy"
        else:
            continue
        
#function to list all the elements in the priority queue        
def list_all(*args):
    text.delete("1.0", END)
    taskList = PriorityQUtils.dump()
    text.insert(CURRENT,"\nDisplaying the whole Priority Queue\n")
    for i in range(len(taskList)):
        if not taskList[i] == []:
            count = len(taskList[i])
            text.insert(CURRENT,"Tasks At priority :" + str(i) + "\n")
            for j in range(count):
                if not taskList[i][j] == []:
                    taskObject = taskList[i][j].get()
                    text.insert(CURRENT,str(taskObject.currentTimeStamp) + "\t" + str(taskObject.description) + "\n\n")

#Defining the root and the UI Elements required           
root = Tk()
root.title("Priority Queue Operations")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Heading
main_title = Label(mainframe, text = "Priority Queue Implementation", relief=RAISED, justify= CENTER, bd = 5)
main_title.grid(column = 4, row =1)

#Put UI elements
put_label = Label(mainframe, text = "Enter the priority ")
put_label.grid(column = 2, row=2, sticky = (W, E))

priority = StringVar()
put_entry = ttk.Entry(mainframe, width = 7, textvariable = priority)
put_entry.grid(column = 3, row = 2, sticky = (W, E))

put_desc_label = Label(mainframe, text = "Enter the Task Description ")
put_desc_label.grid(column = 2, row = 3, sticky = (W, E))

priorityDesc = StringVar()
put_entry_desc = ttk.Entry(mainframe, width = 7, textvariable = priorityDesc)
put_entry_desc.grid(column = 3, row = 3, sticky = (W, E))

ttk.Button(mainframe, text="PUT",command=put).grid(column = 2, row=4, sticky=W)

#text area
text = Text(mainframe)
text.grid(column = 4, row = 6, sticky = (W, E))

#get UI elements
ttk.Button(mainframe, text="GET",command=get).grid(column = 2, row=6, sticky=W)

#list all UI elements
ttk.Button(mainframe, text="LIST ALL",command=list_all).grid(column = 2, row=8, sticky=W)

#binding all elements
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
put_entry.focus()
root.bind('<Return>', put)
root.mainloop()