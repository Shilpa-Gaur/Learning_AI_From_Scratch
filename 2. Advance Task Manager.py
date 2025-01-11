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
   
   VALID_MAIN_MENU = ["1","2", "3", "4", "5","6"]
   while True:
        print("Task Manager Menu")
        print("1. Add New Task")
        print("2. View Tasks")
        print("3. Edit Tasks")
        print("4. Delete Task")
        print("5. Filtered View Tasks")
        print("6. Exit")
        
        user_choice = input ("Choose Option")

        if user_choice == "1":
            add_task()

        elif user_choice == "2":
            view_task()

        elif user_choice == "3":
            edit_task()

        elif user_choice == "4":
            del_task()
        
        elif user_choice == "5":
            filtered_view()
            
        elif user_choice == "6":
            print("Good Bye, Finish Those Tasks")
            break
        
        else:
            print("Invalid Choice")

#let's define edit funtion

VALID_WHAT_TO_EDIT = {"1", "2", "3"}

def edit_task():
    if not task_list:       # If there is no task
        print("No task added")
        return

    view_task()            # Show the task list
    task_to_edit = input("Which task you want to edit?")    #Ask the user for the task list
    try:
        task_no = int(task_to_edit)     #convert the input to numeric form
        if task_no < 1 or task_no > len(task_list):
            print("Wrong task number")
            return
    except ValueError:                  #error message if non-numeric values are given
        print("Please input a valid number")
        return
    
    what_to_edit = input ("What to edit - Choose 1 Name, 2 Priority, 3 Status")
    

    if what_to_edit not in VALID_WHAT_TO_EDIT:
        print("Give correct choic for editing")
        return

    elif what_to_edit == "1":
        edit_task_name = input("Whats the new task name?")
        task_list[task_no -1] ['name'] = edit_task_name
        print("Name edited successfully")
    
    elif what_to_edit == "2":
        edit_task_priority = input ("What's the new task priority, H,M,L")
        while edit_task_priority not in VALID_PRIORITY:
            print ("Assign Valid Priority")
            edit_task_priority = input ("What's the new task priority, H,M,L")
        task_list[task_no -1] ['priority'] = edit_task_priority
        print("Priority edited successfully")
    
    elif what_to_edit =="3":
        edit_task_status = input ("What's the new task status, TD, Started, Done")
        while edit_task_status not in VALID_STATUS:
            print ("Assign Valid Status")
            edit_task_status = input ("What is the task status- TD, Started, Done ?")
        task_list[task_no-1] ['status'] = edit_task_status
        print("Status edited successfully")
        
#lets define delete task function

def del_task():
    if not task_list:
        print("No Task Added")
    
    view_task()     # view all tasks
    task_to_delete = input("Which task to delete ?")    # ask which task to delete

    #convert the user input for task_to_delete in integer and validating if that task no exist

    try:
        task_del_no = int(task_to_delete)
        if task_del_no < 1 or task_del_no > len(task_list):
            print("Wrong task number")
            return
        # print task details
        print(f"\n Task to delete")
        print(f"Task: {task_list[task_del_no -1]['name']}")
        print(f"Priority: {task_list[task_del_no - 1]['priority']}")
        print(f"Status: {task_list[task_del_no - 1]['status']}")

        #confirm if the user really want to delete the task
        confirm = input("\n Do you confirm that you want to delete the task - yes or no")
        if confirm.lower() == "yes":        #learnt a new method for string variable .lower() it will convert user input to lowercase
            del task_list[task_del_no -1]
            print("Task successfully deleted")
        else:
            print("Deletion cancelled")
        
    except ValueError:
        print("Please input a valid number")
        return

#lets define Filtered_view task

def filtered_view():
    if not task_list:
        print("No tasks added")
        return

    #Lets ask which filter to use
    print("Filter by:")
    print("1. Priority")
    print("2. Status")
    
    filter_choice = input("Choose a filter choice 1 or 2")

    if filter_choice == "1":        #filter by priority
        filter_priority = input("Choose valid filter priority - H, M, L")

        while filter_priority not in VALID_PRIORITY:
            print("Choose Valid Filters")
            filter_priority = input("Choose valid filter priority - H, M, L")

    # I am trying to write a function where i want my progrom to choose only those tasks which have filter_priority
        found = False  # I am learning found variable and here we start our for loop with found = false as we have not found anything yet

        for i, task in enumerate(task_list):
            if task['priority'] == filter_priority:
                found = True                        # now if we found the condition we write found true and then what to do if found true
                print(f"{i+1}. Task: {task['name']}")
                print(f"Priority: {task['priority']}")
                print(f"Status: {task['status']}")
                print () # line break between tasks
        
        if not found:
            print("No tasks found")

    elif filter_choice == "2": #filter by status
        filter_status = input("Choose valid filter status - TD, Completed, Done")

        while filter_status not in VALID_STATUS:
            print("Choose Valid Status")
            filter_status = input("Choose valid filter status - TD, Completed, Done")

        #Now, lets put staus filter similar to priority filter
        #again we are initializing found variable by starting with not found

        found = False

        for i, task in enumerate(task_list):
            if task['status'] == filter_status:
                found = True            # if found then detail of what to do
                print(f"{i+1}. Task:{task['name']}")
                print(f"Priority:{task['priority']}")
                print(f"Status:{task['status']}")
                print() # line break between tasks

        if not found:
            print("No taska found")  #message if found is still not true

    else:
        print("Invalid filter Choice")


    # Now i understood that it is a command to python that if this program is being run directly then start with main menu

if __name__ == "__main__":
    main_menu()