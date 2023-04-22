# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date
import copy

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Define reg_user function
# Add a new user to the user.txt file
def reg_user(usernames):

    while True:
        # Request input of a new username and password
        new_username = input("New Username: ")
        new_password = input("New Password: ")

        # Check if username already exists in user.txt
        # If so, add user to enter a different username
        if new_username in usernames:
            print("Sorry, this username already exists in user.txt.\n Please add a different username")
            continue
        # If not, add new user to user.txt
        else:
            with open ("user.txt", "a") as user_file:
                user_file.write(f"\n{new_username};{new_password}")
                print("New user added!")
            break
# Define add_task function
# To add a new task to the task.txt file
# '''Allow a user to add a new task to task.txt file
#            Prompt a user for the following: 
#            - A username of the person whom the task is assigned to,
#             - A title of a task,
#             - A description of the task and 
#             - the due date of the task.'''
def add_task(usernames):
      
    # Ask user to input name of person assigned to task
    # Prompt a user for the following: 
    #    - A username of the person whom the task is assigned to,
    #    - A title of a task,
    #    - A description of the task and 
    #    - the due date of the task.
    task_username = input("Name of person assigned to task: ")

    # Check whether name of person is in the file
    # if not, print out message
    if task_username not in usernames:
        print("This user does not exist.")
    #if yes, request for more inputs of the task    
    else: 
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        task_curr_date = datetime.today()
        task_due_date = input("Due date of task (YYYY-MM-DD): ")
        task_completed = "No"          
       
        # Add new_task into task_list
        # Write into tasks.txt file
        with open("tasks.txt", "a") as task_file:
            task_file.write(f"\n{task_username};{task_title};{task_description};{task_curr_date};{task_due_date};{task_completed}")
            print("Task successfully added.")

# Define view_all function
# '''Reads the task from task.txt file and prints to the console in the 
#           format of Output 2 presented in the task pdf (i.e. includes spacing
#           and labelling) 
#        '''
def view_all (task_list):

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date']}\n"
        disp_str += f"Due Date: \t {t['due_date']}\n"
        disp_str += f"Task Description: \t {t['description']}\n"
        disp_str += f"Task completed: \t {t['completed']}"
        print(disp_str)

# Define view_mine task function
#'''Reads the task from task.txt file and prints to the console in the 
#           format of Output 2 presented in the task pdf (i.e. includes spacing
#           and labelling)
#        '''
def view_mine (curr_user):

    # Open tasks.txt
    # Read contents in tasks.txt
    with open('tasks.txt', 'r') as file:
        contents = ""
        i = 1
        dict_task_list = {}
        for line in file:
            contents = line
            # Convert each task line into a list
            contents_list = contents.split(";")
            # Save each line into dict_task_list, use i as key   
            dict_task_list[i] = [line]   
            # Display all tasks assigned to current user
            # Add task number to each task
            if curr_user == contents_list[0]:
                print("************************")
                print ("Task Number: ", i)
                print ("Task: \t\t\t",contents_list[1])
                print ("Assigned to: \t\t\t",contents_list[0])
                print ("Date Assigned: \t\t\t",contents_list[3])
                print ("Due Date: \t\t\t",contents_list[4])
                print ("Task Description: \t\t\t",contents_list[2])
                print ("Task Complete? \t\t\t",contents_list[5])
                print("************************")
            i = i + 1
    print(f"dict_task_list: {dict_task_list}")

    # Request user to select whether they want to edit a task or return to the main menu
    task_selection = int(input ('''Please choose:
    1) select a specific task by entering a number
    2) '-1' to return to the main menu\n'''))
    
    # Go to main menu if input is -1
    if task_selection == -1:
        return
    # if it is a task number, to go specific task    
    else:
        if task_selection in dict_task_list:
            # Save the selected task into a variable called task_selected
            # Convert task into a list
            task_selected = dict_task_list[task_selection]  
            task_selected_join = ''.join(task_selected)
            print(f"task_selected_join: {task_selected_join}")
            task_selected_list = task_selected_join.split(';')    # Remove \n at the end of the line
            print(f"task_selected_list: {task_selected_list}")
            # Ask user how they would like to edit the task
            option = int(input('''Please select what option you want?
    choose '1' - mark the task as complete
    choose '2' - edit the task
           '''))
           # If user want to make the task as complete
            if option == 1:
                file1 = open('tasks.txt', 'r')
                task_edits = ''
             #   task_selected_join1 = ''.join(dict_task_list[task_selection])
                for line in file1:
                    task_selected_list_edit = task_selected_list
                    
                    if task_selected_join in line:
                        task_selected_list_edit[5] = 'Yes'
                        new_line = ';'.join(task_selected_list_edit)
                        new_line = new_line + '\n'
                        print(f"new_line: {new_line}")

                        with open('tasks.txt', 'w') as file11:
                            file11.write(new_line)
                    else:
                        file11 = open('tasks.txt', 'a')
                        file11.write(line)
                        file11.close()
                file1.close()
            
            # if the user choose 2 to edit the task
            else:
                file1 = open('tasks.txt', 'r')
                # Ask whether user want to change 'username' or 'due date'
                edit_selection = input ("What do you want to change: choose 'username' or 'due date':\n")
                # If user select to change 'username'
                if edit_selection.lower() == 'username':
                    new_username = input("New name of person assigned to task: ")
                    task_selected_list_edit = task_selected_list
                    # Use a for loop, go through each line in tasks.txt
                    for line in file1:
                        # if the line is the selected task
                        if task_selected_join in line:
                            if 'No' in line:
                                task_selected_list_edit[0] = new_username
                                new_line = ';'.join(task_selected_list_edit)
                                print(f"new_line: {new_line}")
                                with open('task.txt', 'w') as file11:
                                    file11.write(new_line)

                            else:
                                print("This task is completed already")
                        # if the line is not the selected task
                        # just write it in the file
                        else:
                           file11 = open('tasks.txt', 'a')
                           file11.write(line)
                           file11.close()

                # If user select to change 'due date'
                else:
                    new_duedate = input("New due date of task (YYYY-MM-DD): ")
                    task_selected_list_edit = task_selected_list
                    # Use a for loop, go through each line in tasks.txt
                    for line in file1:
                        if task_selected_join in line:
                            if 'No' in line:
                                task_selected_list_edit[4] = new_duedate
                                new_line = ';'.join(task_selected_list_edit)
                                print(f"new_line: {new_line}")

                                with open('task.txt', 'w') as file11:
                                    file11.write(new_line)

                            else:
                                print("This task is completed already")
                        else:
                            file11 = open('tasks.txt', 'a')
                            file11.write(line)
                            file11.close()    



def generate_report (usernames, task_list):
    # generate reports
    # write into task_overview.txt file, it should contain:
    # - total number of tasks that have been generated and tracked using the task_manager.py
    # - the total number of completed tasks
    # - the total number of uncompleted tasks
    # - the total number of tasks that haven't been completed and that are overdue
    # - the percentage of tasks that are incomplete
    # - the percentage of tasks that are overdue

    # define relevant variables
    total_tasknumber = 0
    total_completed = 0
    total_uncompleted = 0
    total_overdue = 0

        # use a for loop, to count relevant numbers
    for t in task_list:
        total_tasknumber += 1
        if t['completed'] == 'Yes':
            total_completed += 1
        else:
            total_uncompleted += 1

            #check if a task haven't been completed and are overdue
            #Question: how to convert due date in to dateformat to compare?
            if datetime.strptime(t['due_date'][0:10], DATETIME_STRING_FORMAT) <= datetime.today():
                total_overdue += 1

        # calculate percentage of tasks that are incomplete
        # calculate percentage of tasks that are overdue            
        perc_uncompleted = (total_uncompleted/total_tasknumber)*100
        perc_overdue = (total_overdue/total_tasknumber)*100

    task_overview = f'''\nThe total number of tasks that have been generated and tracked using the task_manager.py: {total_tasknumber}
The total number of completed tasks: {total_completed}
The total number of uncompleted tasks: {total_uncompleted}
The total number of tasks that haven't been completed and that are overdue: {total_overdue}
The percentage of tasks that are incomplete: {perc_uncompleted}%
The percentage of tasks that are overdue: {perc_overdue}%
        '''
    f = open("task_overview.txt", "w+")
    f.write(task_overview)
    f.close()

    #write into user_overview.txt file
    user_number = 0
    total_user = 0
    user_task = {}
    all_user_task = []


    #Question: how to only count for each user?
    print(f"usernames: {usernames}")
    for username in usernames:
        user_number += 1
        total_user_tasknumber = 0
        perc_user_tasknumber = 0
        user_tasknumber_completed = 0
        user_tasknumber_tocomplete = 0
        user_tasknumber_due = 0
 

        for t in task_list:
            if t['username'] == username:
                total_user_tasknumber += 1
                if t['completed'] == 'Yes':
                    user_tasknumber_completed += 1
                else:
                    user_tasknumber_tocomplete += 1
                  

                    #Question: how to compare date
                    # convert str date into date type?
                    if datetime.strptime(t['due_date'][0:10], DATETIME_STRING_FORMAT) < datetime.today():
                        user_tasknumber_due += 1
        perc_user_tasknumber = (total_user_tasknumber/total_tasknumber)*100
        perc_user_tasknumber_completed = (user_tasknumber_completed/total_tasknumber)*100
        perc_user_tasknumber_tocomplete = (user_tasknumber_tocomplete/total_tasknumber)*100
        perc_user_trasknumber_due = (user_tasknumber_due/total_tasknumber)*100
        user_task = {'username': username, 'usertasknumber': total_user_tasknumber, 'perc_user_tasknumber': perc_user_tasknumber,
            'perc_user_tasknumber_completed': perc_user_tasknumber_completed, 
            'perc_user_tasknumber_tocomplete': perc_user_tasknumber_tocomplete,
            'perc_user_tasknumber_overdue': perc_user_trasknumber_due}
        all_user_task.append(user_task)
        
    user_overview = f'''The total number of users registered with task_manager.py is: {user_number}
The total number of tasks that have been generated and tracked using the task_manager.py: {total_tasknumber}
                '''
    h = open("user_overview.txt", "w+")
    h.write(user_overview)
    h.close()
    for i in all_user_task:
        user_info = f'''\n\nOverview for user {i['username']}:
The total number of tasks is: {i['usertasknumber']}
The percentage of the total number of tasks is: {i['perc_user_tasknumber']}%
The percentage of the the tasks that have been completed is: {i['perc_user_tasknumber_completed']}%
The percentage of the tasks that must still be completed is: {i['perc_user_tasknumber_tocomplete']}%
The percentage of the tasks that have not yet been completed and are overdue is: {i['perc_user_tasknumber_overdue']}% 
            \n'''
        h = open("user_overview.txt", "a")
        h.write(user_info)
        h.close()
                    

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass
# read tasks.txt
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = task_components[3]
    curr_t['assigned_date'] = task_components[4]
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    
    print(f"curr_t: {curr_t}")
    task_list.append(curr_t)  #save into task_list



#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
# Save username into usernames
usernames = []
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password
    usernames.append(username)

# Use a while loop check login
logged_in = False
while not logged_in:
    print("LOGIN")
    # request user for input 
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    # check whether entered username and password matches with stored information
    # if no, print relevant messages out
    # otherwise, print 'login succesful' and change logged_in into 'True'
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while logged_in:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    # when user is admin, use menu below:
    if curr_user.lower() == 'admin':
        menu = input('''Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
: ''').lower()
    # when user is not admin, use menu below:
    else:
        menu = input('''Select one of the following Options below:
a - add task
va - view all tasks
vm - view my task
e - Exit
: ''').lower()

    # r - Registering a user
    if menu == 'r':
        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        reg_user(usernames)
       
    # a - Adding a task
    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        add_task(usernames)
        

    # va - View all tasks
    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
        view_all (task_list)
            
    # vm - view my task
    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine (curr_user)
       
    elif menu == 'gr':
        # generate reports
        # write into task_overview.txt file, it should contain:
        # - total number of tasks that have been generated and tracked using the task_manager.py
        # - the total number of completed tasks
        # - the total number of uncompleted tasks
        # - the total number of tasks that haven't been completed and that are overdue
        # - the percentage of tasks that are incomplete
        # - the percentage of tasks that are overdue
        print(f"usernames: {usernames}")
        generate_report (usernames, task_list)

    
    # display statistics          
  
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
            generate_report (usernames, task_list)

        with open("task_overview.txt", "r") as task_file:
            task_file_contents = task_file.read()
            print (task_file_contents)
        
        print("-----------------------------------")

        with open("user_overview.txt", "r") as user_file:
            user_file_contents = user_file.read()
            print (user_file_contents)



    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


