import sys

#Function that checking if the user input is a number
def is_a_number(element):
    try:
        int(element)
        return True
    except:
        try:
            float(element)
            return True
        except:
            pass
        print(f'{element} it isnt a number!')
        sys.exit(0)

#Function that checking if the user input is an expected mathematical operation
def check_math_operation(operation):
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        return True
    else:
        print("It isnt expected mathematical operation!")
        sys.exit(0)

#Function that checking type of variables (float or int) and doing operaiton
def do_operation(first_number,second_number,operation):
    global result

    try:
        first_number = int(first_number)
        second_number = int(second_number)
        if operation == "+":
            result = int(first_number) + int(second_number)
        elif operation == "-":
            result = int(first_number) - int(second_number)
        elif operation == "*":
            result = int(first_number) * int(second_number)
        elif operation == "/":
            if int(second_number) == 0:
                print("You cant divide by 0")
                sys.exit(0)
            else:
                result = int(first_number) / int(second_number)
    except:
        first_number = float(first_number)
        second_number = float(second_number)
        if operation == "+":
            result = float(first_number) + float(second_number)
        elif operation == "-":
            result = float(first_number) - float(second_number)
        elif operation == "*":
            result = float(first_number) * float(second_number)
        elif operation == "/":
            if float(second_number) == 0.0:
                print("You cant divide by 0")
                sys.exit(0)
            else:
                result = float(first_number) / float(second_number)
                
#Getting first number from user
first_number = input("Enter your first number: ")

#Declaring second_number variable which will contain second number of operation
second_number= 0

#Declaring mathematical_operation variable which will contain operation which user entered
mathematical_operation = ""

#Declaring result variable which contain operation result
result = 0



if is_a_number(first_number) is True:
    second_number = input("Enter your second number: ")
    if is_a_number(second_number) is True:
        mathematical_operation = input("Which mathematical operation do you want to use? + ; - ; * ; / ")
        if check_math_operation(mathematical_operation) is True:
            do_operation(first_number,second_number,mathematical_operation)
            print(f'Your result is {result}')
            sys.exit(0)




    




