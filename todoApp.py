added_tasks = []
def addtask():
    a = input("Add task")
    print("Task added:", a)
    added_tasks.append(a)
    print("All tasks:", added_tasks)
    print(repeat())
def repeat():
    b = input("Press 1 to add another task or 2 to complete your task")
    print(b)
    if b == "1":
        addtask()
    elif b == "2":
        a = input("Enter the task you have completed")
        added_tasks.remove(a)
        print("Your remaining tasks are", added_tasks)
print(addtask())