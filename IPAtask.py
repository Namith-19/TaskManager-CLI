import pandas as pd
try:
    taskdf=pd.read_csv("Tasks.csv")
except :
    taskdf=pd.DataFrame({"Date":[],"Task":[],"Status":[]})
    taskdf.to_csv("Tasks.csv")

def addTask():
    global taskdf
    inpTask=str(input("Enter the Task: "))
    inpDate=str(input("Enter the date for the Task Format(dd/mm/yyyy): "))
    try:
        temp=inpDate.split("/")
    except:
        print("Enter valid details")
    if(int(temp[0])>31 or int(temp[1])>12 or int(temp[2]) not in range(1000,10000)):
        print("Enter the correct date with format(dd/mm/yyyy)")
    elif(len(inpTask)==0):
        print("Enter valid task details")
    else:
        if(len(taskdf.index)==0):
            taskdf.loc[0]=[inpDate,inpTask,"Not Completed"]
        else:
            taskdf.loc[max(taskdf.index)+1]=[inpDate,inpTask,"Not Completed"]
        print("Entered task")

def displayTasks():
    global taskdf
    if(len(taskdf.index)!=0):
        print(taskdf)
    else:
        print("There are no tasks to display\n")

def markCompleted(indx):
    if(len(taskdf.index)!=0):
        taskdf["Status"].iloc[indx]="Completed"
    else:
        print("There are no tasks to mark as complete\n")
  
def deleteTask(indx):
    global taskdf
    if(len(taskdf.index)!=0):
        if(taskdf["Status"].loc[indx].lower()!="completed"):
            if(str(input("The task is not completed are you sure you want to delete(Y/N): ")).lower()=="y"):
                taskdf.drop(index=indx,axis=0,inplace=True)
            else:
                pass
        else:
                taskdf.drop(index=indx,axis=0,inplace=True) 
    else:
        print("There are no tasks to delete\n")
    
def saveTasks():
    global task,taskdf
    taskdf.to_csv("Tasks.csv",index=False)

def readTask():
    global taskdf
    taskdf=pd.read_csv("Tasks.csv")

def console():
    choice=int(input("Choices:\n1:Add task\n2:Display tasks\n3:Mark task as completed\n4:Delete task\n5:Exit\nEnter the choice: "))
    match(choice):
        case 1:
            addTask()
            console()
        case 2:
            displayTasks()
            console()

        case 3:
            markCompleted(int(input("Enter the index for completion of the task: ")))
            console()

        case 4:
            deleteTask(int(input("Enter the index for deletion of the task: ")))
            console()

        case 5:
                pass
        case _:
            print("Enter the correct choice")
            console()

console()
saveTasks()
