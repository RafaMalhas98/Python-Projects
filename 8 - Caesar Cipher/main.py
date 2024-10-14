import  art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    shifted_text = ""

    for letter in original_text:
        if letter in alphabet:
            #Checks the index for the current letter
            current_index = alphabet.index(letter)
            if encode_or_decode == "encode":
                #New index is equal to the current letter index plus the shift amount given by the user
                shifted_index = current_index + shift_amount
            else:
                # New index is equal to the current letter index minus the shift amount given by the user
                shifted_index = current_index - shift_amount
            #Returns the module to always get the index in the length range. Ex: shift = 70, range = 26 => 70 % 26 = 18, it means that the new index will be 18
            shifted_index %= len(alphabet)
            #Concatenates the new letter to the string
            shifted_text += alphabet[shifted_index]
        else:
            shifted_text += letter
    print(f"Here is the {direction}d result: {shifted_text}")


is_to_continue = True

while is_to_continue:
    valid_option = False
    #As long as the user doesn't select the correct option, it continues to ask for the direction
    while not valid_option:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        #Checks if the user selected one of the options
        if direction == "encode" or direction == "decode":
            valid_option = True
        else:
            print("Please choose a valid option.")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    valid_option = False
    # As long as the user doesn't select the correct option, it continues to ask for the user_continue
    while not valid_option:
        user_continue = input("Do you want to continue? Type \'Yes' to continue or \'No' to end\n").lower()
        # Checks if the user selected one of the options
        if user_continue == "yes":
            is_to_continue = True
            valid_option = True
        elif user_continue == "no":
            is_to_continue = False
            valid_option = True
        else:
            print("Please choose a valid option.")



