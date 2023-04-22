# Define a function to display answer to the equation
# and to write equation to the file named 'equations.txt'
def write_equation(num1, num2, operator, answer):
    print(f"{num1} {operator} {num2} = {answer}")
    file = open("equations.txt", "a")
    file.write(f"{num1} {operator} {num2}\n")
    file.close

# Define a calculator
# Use inputs (two numbers, and one operator) from the user
def calculator (num1, num2, operator):
    if operator == '+':
        answer = num1 + num2
        # Call function write_equation to display answer and write into the file named 'equations.txt'
        write_equation(num1, num2, operator, answer)

    elif operator == '-':
        answer = num1 - num2
        write_equation(num1, num2, operator, answer)
       
    elif operator == '*':
        answer = num1 * num2
        write_equation(num1, num2, operator, answer)
    elif operator == '/':
        # When operator is '/', use try except in case the second number is 'Zero' that cannot be divided
        try:
            answer = num1 / num2
            write_equation(num1, num2, operator, answer)           
        except ZeroDivisionError:
            print("Ohh, 'Zero' cannot be divided.")            
    else:
        print("Sorry, please select operator with given choices")

# Request input from the user 
# to select from option 'A' and option 'B'   
option = input('''Please select your choice:
- option 'A': enter two numbers and an operator
- option 'B': read all the equations from a txt file\n''')
if option == 'A':
    # If user selected option 'A', request user to input two numbers and an operator
    # Use a while loop to make sure user input right format of two numbers
    # Use try except if user input wrong format of a number
    while True:
        try:
            num1 = int(input ("please enter the 1st number:"))
            num2 = int(input ("please enter the 2nd number:"))
            break
        except Exception:
            print("Ohh, that was not a valid number, please try again...")
    operator = input("Please enter the operation(e.g. +, -, *, / etc.:")
    # Call function calculator to calculat inputs from user
    calculator(num1, num2, operator)
elif option == 'B':
    # If user selected option 'B', request user to input a file name
    file_name = input("Please enter a new file name:") 
    # Use try except in case a file name does not exist
    try:
        file = open(file_name, 'r')
    except Exception:
        print('You entered wrong file name.')
        exit()
    # Save each line into a list called contents
    contents = []
    for line in file:
        contents.append(line[:-1])
    
    # To read each item in the string
    # Convert string into list
    # Convert items in the list into right format for the equation     
    for content in contents:
        equation_list = content.split(' ')
        # Use try except in case the format of items in the list is not correct
        try:
            number1 = int(equation_list[0])
            number2 = int(equation_list[2])
            operator = equation_list[1]
        except Exception:
            print('The format of equation in the file is incorrect.')
            exit()
        # Call function calculator to calculat inputs from user
        calculator(number1, number2, operator) 
   
else:
    print("Sorry, your selection is not valid, please try again.")
