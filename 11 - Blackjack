import art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
aux_cards = cards
def deal_cards(number_of_cards, list_of_cards):
    """Function to deal x cards and stores it into a list. Returns the list of cards. If the length of the list is less than 12, it replaces with a new deck"""
    global aux_cards
    global cards
    #Checks if the list of cards have at least 12 cards
    if len(cards) < 12:
        cards = aux_cards
    cards_list = list_of_cards
    #Deals x amount of cards
    for _ in range (number_of_cards):
        #Save the random card into a variable
        card_picked = random.choice(cards)
        #Appends it to the output list
        cards_list.append(card_picked)
        #Removes it from the original list
        cards.remove(card_picked)
    return cards_list

def validate_cards(list_of_cards):
    """Function to see if the list contains a blackjack (A,10)"""
    is_blackjack = False
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        is_blackjack = True
    return is_blackjack

def validate_blackjack(user_is_blackjack, pc_is_blackjack):
    """Function to check for the user and pc blackjack. Possibilities: user and not pc > 0 / user and pc > 1 / else > 2"""
    if user_is_blackjack and not pc_is_blackjack:
        return 0
    elif user_is_blackjack and pc_is_blackjack:
        return 1
    else:
        return

def calculate_card_scores(list_of_cards):
    """Function to return the sum of the card in the list"""
    score = sum(list_of_cards)
    if score > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        score = sum(list_of_cards)

    return score


def blackjack():
    global user_amount
    global user_bet
    user_card_list = []
    pc_card_list = []

    valid_option = False
    #Loop to check if the user inputs a valid bet
    while not valid_option:
        try:
            user_bet = int(input("How much do you want to bet? => "))
            if user_bet <= user_amount:
                #Breaks the loop
                valid_option = True
                #Subtract the bet on the amount
                user_amount -= user_bet
            else:
                print("You don't have that amount")
        except ValueError:
            print("\nPlease provide a valid option.")

    os.system('cls')

    print(art.logo)

    #Calls the function to deal 2 random cards to the user
    user_card_list = deal_cards(2, user_card_list)
    #Calls the function to deal 2 random cards to the pc
    pc_card_list = deal_cards(2, pc_card_list)
    #Calls the function to validate if the user have a blackjack
    user_cards_validation = validate_cards(user_card_list)
    #Calls the function to validate if the pc have a blackjack
    pc_cards_validation = validate_cards(pc_card_list)
    #Calls the function to return the user cards score
    user_score = calculate_card_scores(user_card_list)
    #Calls the function to return the pc cards score
    pc_score = calculate_card_scores(pc_card_list)
    print(f"\nYour cards: {user_card_list}, current score: {user_score}")
    print(f"Computer's first card: {pc_card_list[0]}")
    #Calls the function to validate the user and pc possible blackjack
    out_validate_blackjack = validate_blackjack(user_cards_validation, pc_cards_validation)
    if out_validate_blackjack == 0:
        print("Win with a Blackjack!")
        user_amount = (user_bet *2 )
        return
    elif out_validate_blackjack == 1:
        print("Computer got a blackjack. You Lose")
        return

    is_to_continue = True
    pc_played = False
    #Loop to check if the user inputs a valid choice
    while is_to_continue:
        user_option = input("\nType 'y' to get another card, type 'n' to pass => ").lower()

        if user_option == "y":
            #Calls the function to deal 1 random cards to the user
            user_card_list = deal_cards(1, user_card_list)
            #Calls the function to return the user cards score
            user_score = calculate_card_scores(user_card_list)
            os.system('cls')
            print(art.logo)
            print(f"\nYour cards: {user_card_list}, current score: {user_score}")
            print(f"Computer's hand: {pc_card_list[0]}")
            if user_score > 21:
                print("You went over. You Lose")
                return

        elif user_option == "n":
            while pc_score < 16:
                #Calls the function to deal 1 random cards to the pc
                pc_card_list = deal_cards(1, pc_card_list)
                #Calls the function to return the pc cards score
                pc_score = calculate_card_scores(pc_card_list)
            os.system('cls')
            print(art.logo)
            print(f"\nYour cards: {user_card_list}, current score: {user_score}")
            print(f"Computer's hand: {pc_card_list}, current score: {pc_score}")
            if pc_score > 21:
                print("Computer went over. You Win")
                return
            pc_played = True
        else:
            print("Please provide a valid option.\n")

        #Checks the winner
        if pc_played:
            if user_score > pc_score:
                print("You Win")
                user_amount += (user_bet * 2)
                return
            elif user_score == pc_score:
                print("It's a draw")
                return
            else:
                print("You Lose")
                return




print(art.logo)
valid_option = False
user_amount = 0
user_bet = 0

#Loop to check if the user inputs a valid amount
while not valid_option:
    try:
        user_amount = int(input("With how much do you want to enter the table? => "))
        #Breaks the loop
        valid_option = True
    except ValueError:
        print("\nPlease provide a valid option.")

blackjack()
print(f"Remaining Amount: {user_amount}")
#print(cards)
#if user_amount > 0:
valid_option = False
if user_amount > 0:
    #Loop to check if the user inputs a valid amount
    while not valid_option:
        new_round = input("\nDo you want to play another round? Type 'y' or 'n' => ").lower()
        if new_round == "y":
            blackjack()
            print(f"Remaining Amount: {user_amount}")

        elif new_round == "n":
            #Breaks the loop
            valid_option = True
        else:
            print("Please provide a valid option.\n")
    else:
        print("You don't have enough credits to play.")
