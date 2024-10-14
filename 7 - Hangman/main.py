import random
import hangman_words
import hangman_art

#Imports the word list
word_list = hangman_words.word_list
#Sets the number of lives
lives = 6

print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

#Creates a placeholder
for position in chosen_word:
    placeholder += "_"


#Creates a list of the placeholder characters
placeholder_list = list(placeholder)

#Creates a list of letters tried and letters failed
letters_tried_list = []
letters_failed_list = []

#While the placeholder has '_' in it and the lives are more than zero, executes the code
while '_' in placeholder and lives > 0:

    #letter_index > To iterate the placeholder list
    #letter_found > To check if the letter was found
    letter_index = 0
    letter_found = False

    print(f"Word to guess: {placeholder}")
    #Asks the user for a letter
    guess = input("Guess a letter: ").lower()

    #Checks if the user already choose that letter
    if guess in letters_tried_list:
        print("You already choose that letter.")
    else:
        #Iterate every letter in the random word
        for letter in chosen_word:
            if letter == guess:

                #Replace the '_' with the guess letter
                placeholder_list[letter_index] = guess
                #Change the letter_found value
                if not letter_found:
                    letter_found = True

            letter_index += 1

        #If the letter haven't been found: 1)One less live 2)Append the guess letter to the failed letters list
        if not letter_found:
            lives -= 1
            letters_failed_list.append(guess)

        #Appends the letter guess to the letters tried list
        letters_tried_list.append(guess)

        #Convert the placeholder list into a string
        placeholder = "".join(placeholder_list)
        print(placeholder)
        print(f"{hangman_art.stages[lives]}")
        print(f"Letters failed: {letters_failed_list}")
        print(f"****************************{lives} LIVES LEFT****************************")

if lives == 0:
    print("***********************YOU LOSE**********************")
    print(f"The correct word was <{chosen_word}>")
else:
    print("****************************YOU WIN****************************")
