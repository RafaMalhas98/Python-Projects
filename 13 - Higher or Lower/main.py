import art
import game_data
import random
import os
print(art.logo)
def get_random_choice():
    """Function that generates a random choice from the list and returns a list"""
    choice = random.choice(game_data.data)
    return choice

def validate_choices(first_choice, second_choice):
    """Function that verifies if the two choices are equal, and returns True if the choices are different or False if the choices are the same"""
    if first_choice == second_choice:
        return False
    else:
        return True

def concatenate_choice(choice_list):
    """Function to return a string with the name, description and country concatenated, and an integer that stores the followers count"""
    choice_string = choice_list["name"] + ", a " + choice_list["description"] + ", from " + choice_list["country"]
    choice_value = choice_list["follower_count"]
    return choice_string, choice_value

def validate_higher_lower(choice_user, choice_other):
    """Function to check which choice have the most followers, and returns True the user guessed correctly, False if the user guessed wrong"""
    if choice_user >= choice_other:
        return True
    else:
        return False

def higher_lower():
    is_to_continue = True
    #Variable to store the user score
    user_score = 0
    #Variable to store the user choice
    user_choice = ""
    #Variable to store the other choice
    remain_choice = 0
    list_choice_a = []
    list_choice_b = []
    is_first_round = True

    while is_to_continue:
        if is_first_round:
            #Variable to store the first choice generated
            list_choice_a = get_random_choice()
            #Variable to store the value of the generated choice
            choice_a_string, choice_a_value = concatenate_choice(list_choice_a)
            #print(f"Compare A: {choice_a_string}")
            #print(choice_a_value)
            #print(art.vs)
            # Variable to store the second choice generated
            list_choice_b = get_random_choice()
            # Variable to store the value of the generated choice
            choice_b_string, choice_b_value = concatenate_choice(list_choice_b)
            #print(f"Compare B: {choice_b_string}")
            #print(choice_b_value)
            is_first_round = False
        else:
            list_choice_a = list_choice_b
            # Variable to store the value of the generated choice
            choice_a_string, choice_a_value = concatenate_choice(list_choice_a)
            # Variable to store the second choice generated
            list_choice_b = get_random_choice()
            # Variable to store the value of the generated choice
            choice_b_string, choice_b_value = concatenate_choice(list_choice_b)
        print(f"Compare A: {choice_a_string}")
        print(art.vs)
        print(f"Compare B: {choice_b_string}")

        #Calls the function to check if the generated choices are the same, if they are the same, generates another two
        if not validate_choices(list_choice_a,list_choice_b):
            # Variable to store the first choice generated
            list_choice_a = get_random_choice()
            # Variable to store the value of the generated choice
            choice_a_string, choice_a_value = concatenate_choice(list_choice_a)
            print(f"Compare A: {choice_a_string}")
            # print(choice_a_value)
            print(art.vs)
            # Variable to store the second choice generated
            list_choice_b = get_random_choice()
            # Variable to store the value of the generated choice
            choice_b_string, choice_b_value = concatenate_choice(list_choice_b)
            print(f"Compare B: {choice_b_string}")
            # print(choice_b_value)

        valid_option = False

        #Loop to check if the user choose a valid option
        while not valid_option:
            user_choice = input("\nWho has more followers? Type 'A' or 'B' => ").upper()
            if user_choice == "A":
                user_choice = choice_a_value
                remain_choice = choice_b_value
                valid_option = True
            elif user_choice == "B":
                user_choice = choice_b_value
                remain_choice = choice_a_value
                valid_option = True
            else:
                print("Please provide a valid option.\n")

        os.system('cls')
        print(art.logo)

        #Calls the function to validate which choice is higher
        if validate_higher_lower(user_choice, remain_choice):
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            is_to_continue = False

higher_lower()

valid_option = False
#Loop to check if the user choose a valid option
while not valid_option:
    restart_game = input("\nDo you want to restart? Type 'Y' or 'N' => ").upper()
    if restart_game == "Y":
        os.system('cls')
        print(art.logo)
        higher_lower()
    elif restart_game == "N":
        valid_option = True
    else:
        print("Please provide a valid option.")
