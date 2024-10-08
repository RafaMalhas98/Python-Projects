import art

#Creates a list of the valid mathematical operations
math_operations = ["+", "-", "*", "/", "%"]

def add(n1, n2):
    """Function to add n1 and n2"""
    total = n1 + n2
    return total

def sub(n1, n2):
    """Function to subtract n1 and n2"""
    total = n1 - n2
    return total

def mult(n1, n2):
    """Function to multiply n1 and n2"""
    total = n1 * n2
    return total

def div(n1, n2):
    """Function to subtract n1 and n2"""
    total = n1 / n2
    return total

def mod(n1, n2):
    """Function to get the module of n1 and n2"""
    total = n1 % n2
    return total

#Creates a dictionary with the key(operator)-value(function name) pairs
calc = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div,
    "%" :   mod,
}

#Variable to check if the user wants the program to continue after every execution
is_to_continue = True
#Variable to check if the user executed the program for the first time
is_first_run = True
print(art.logo)

while is_to_continue:
    valid_option = False

    #If it's the first time, it asks for the first number
    while is_first_run:
        #Loop to check if the input is a float number
        while not valid_option:
            try:
                first_num = float(input("\nWhat's the first number?: => "))
                #The next time the user runs the program using the calculated value it skips this loop
                is_first_run = False
                #Breaks the validation loop
                valid_option = True
            #If the compiler cannot convert the input to a float it means that the input is invalid
            except ValueError:
                print("Please provide a valid number.")

    #Resets the variable
    valid_option = False

    #Prints every possible mathematical operations
    for x in math_operations:
        print(x)

    #Loop to check if the input is a valid mathematical operations
    while not valid_opti8on:
        operator = input("\nPick an operation: ")
        if operator in math_operations:
            #Breaks the validation loop
            valid_option = True
            #Variable to store the function name
            operation = calc[operator]
        else:
            print("Please provide a valid option")

    # Resets the variable
    valid_option = False
    # Loop to check if the input is a float number
    while not valid_option:
        try:
            second_num = float(input("\nWhat's the second number?: => "))
            # Breaks the validation loop
            valid_option = True
        # If the compiler cannot convert the input to a float it means that the input is invalid
        except ValueError:
            print("Please provide a valid number.")

    print(f"{first_num} {operator} {second_num} = {operation(first_num,second_num)}")
    user_option = input(f"Type 'y' to continue calculating with {operation(first_num,second_num)}, type 'n' to start a new calculation, or type 'stop' to end. => ").lower()

    #Checks if the user want to use the calculated value
    if user_option == "y":
        first_num = operation(first_num,second_num)
    #Resets the value and asks again for the first number
    elif user_option == "n":
        is_first_run = True
    #Break the main loop
    else:
        is_to_continue = False



