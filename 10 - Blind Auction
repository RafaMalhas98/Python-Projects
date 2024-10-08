import os
import art
print(art.logo)
print("Welcome to the secret auction program.")

is_to_continue = True
#Creates a new dictionary
bids = {}

#Creates a function that have 2 inputs: name and bid
def add_bids(user_name, user_bid):
    #Adds a new key-value pair to the dictionary
    bids[user_name] = user_bid

#Creates a function that have 1 input: dic_name
def find_max_value(dic_name):
    max_value = 0
    winner = ""
    #Iterates all pairs of the dictionary and checks if the value is higher than max_value
    for key in bids:
        if dic_name[key] > max_value:
            max_value = dic_name[key]
            winner = key
    print(f"The winner is {winner} with the highest bid of: {max_value}")

while is_to_continue:
    valid_option = False
    #Asks the user for the name and bid
    name = input("What is your name? => ")
    price = int(input("What's your bid? => "))

    #Calls the add_bids function and passes the inputs to it
    add_bids(user_name=name,user_bid=price)

    while not valid_option:
        #Asks the user if he wants to continue
        is_to_continue = input("Are there any other bidders? Type 'yes' or 'no' => ").lower()
        if is_to_continue == "yes":
            is_to_continue = True
            valid_option = True
        elif is_to_continue == "no":
            is_to_continue = False
            valid_option = True
        else:
            print("Please choose a valid option")
    #Clears the screen
    os.system('cls')

find_max_value(bids)










