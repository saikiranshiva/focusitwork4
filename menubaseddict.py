task={}
while True:
    print("******* My To Do App *********")
    print("1.Add Task")
    print("2.View All Task")
    print("0.Exit")

    ChooseOption=int(input("enter your option"))
    if ChooseOption==1:
            taskname=input("enter task name:")
            ddate=(input("enter date:"))
            task[taskname]=ddate
            print("Task Added")


    elif ChooseOption==2:
        print(task)
   
    elif ChooseOption==0:
        print("Bye")
    else:
        print("Invalide input") 









































