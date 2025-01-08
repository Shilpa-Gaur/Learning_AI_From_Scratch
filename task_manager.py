#project Command Line Task Manager
#A program which takes taks and show their status and priorties
task_list = [] # This creates a list
VALID_PRIORITIES = {"H", "L", "M"}  # Using a set to store valid priorities

VALID_STATUS = {"TO_DO", "COMPLETED", "STARTED"} #using a set to store valid status

#lets define first function

def add_task():
    task_name = input ("What is the task?")
    task_priorities = input ("Give task priority - H,L, M")
    while task_priorities not in VALID_PRIORITIES:
        print ("Wrong Task Priority")
        task_priorities = input ("Give task priority - H,L, M")
    task_status = input ("Give task status- TO_DO,COMPLETED,STARTED")
    while task_status not in VALID_STATUS:
        print ("Wrong Task Status")
        task_status = input ("Task status (TO_DO,COMPLETED,STARTED)")

    new_task = { "name":task_name, "priority": task_priorities, "status":task_status }
    task_list.append(new_task)

    print("Task successfully added")

def view_task():
    if not task_list:
        print("No tasks added")
    else:
        for i, task in enumerate(task_list):
            print ( f"Task: {task['name']}")
            print (f"Status: {task['status']}")
            print (f"Priority: {task['priority']}")
            print()  # blank line between tasks

def main_menu():

    VALID_MAIN_MENU = {"1","2","3"}
    while True:
        print("Task Manager Menu")
        print ("1.Add Task")
        print("2.View Task")
        print("3.Exit")

        user_choice = input("Choose one option")

        if user_choice == "1":
            add_task()
        elif user_choice == "2":
            view_task()
        elif user_choice == "3":
            print( "Bye, Finish Those Tasks")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main_menu()
