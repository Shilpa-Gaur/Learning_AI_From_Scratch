#Testing the Task Manager Code
#Step 1 - Define task_list Variable which will be a list
task_list = []

# Step 2 - Define Valid Menu Options, Status & Prioriities
VALID_PRIORITY = ["H","M","L"]
VALID_STATUS =["TD", "Started", "Done"]

#Step 3 - Define New task creation Function

def add_task():
    task_name = input ("What is the task?")

    task_priority = input ("What is the task priority, H,M,L?")

    while task_priority not in VALID_PRIORITY:
        print ("Assign Valid Priority")
        task_priority = input ("What is the task priority, H,M,L")

    task_status = input ("What is the task status- TD, Started, Done ?")

    while task_status not in VALID_STATUS:
        print ("Assign Valid Status")
        task_status = input ("What is the task status- TD, Started, Done ?")

    new_task = {'name':task_name, 'priority':task_priority, 'status':task_status}

    task_list.append(new_task)
    print ("New Task Added Successfully")


def view_task():
    if not task_list:
        print("No Tasks Assigned")
#Now this is what i am learning - For Loop, 
    else:
        for i, task in enumerate(task_list):
            print(f"{i+1}. Task: {task['name']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print () # line break between tasks
#in the above function, we understood that we are actually printing the task list one by one from the variable task_list which is a dictionary

#Lets now understand about Defining the main menu

def main_menu():
   
   VALID_MAIN_MENU = ["1","2", "3"]
   while True:
        print("Task Manager Menu")
        print("1. Add New Task")
        print("2. View Tasks")
        print("3. Exit")
        
        user_choice = input ("Chose Option")

        if user_choice == "1":
            add_task()

        elif user_choice == "2":
            view_task()
        
        elif user_choice == "3":
            print("Good Bye, Finish Those Tasks")
            break
        else:
            print("Invalid Choice")

#let's define edit funtion

#def edit_task():


    #I still do not understand this Below code ( It is like a start button for the program)

if __name__ == "__main__":
    main_menu()