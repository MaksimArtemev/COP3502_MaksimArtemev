# Written by Artemev Maksim Alexandrovich

def encode(password):
    # Check if the password is 8 digits long and contains only integers
    if len(password) != 8 or not password.isdigit():
        raise ValueError("Password should be an 8-digit string containing only integers")

    # Encode the password by shifting each digit up by 3 numbers
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3)%10
        encoded_password += str(encoded_digit)

    return encoded_password

def decode(password): # Decodes and presents the original and encoded password
    originalPass = ""
    for val in password: # Reversing the encoding by substracting rather than adding the value
        originalPass += str((int(val) - 3)%10)
    
    print(f"The encoded password is {password}, and the original password is {originalPass}.\n")
    
    

def print_menu(): # menu
    print("Menu\n----------\n1. Encoder\n2. Decoder\n3. Exit\n")

def readIn_user_input(): # Reads the user menu input
    user_input = int(input("Enter 1 or 2: "))
    return user_input

def user_input_validation(user_menu_choice): # Validates the user input
    while 3 < user_menu_choice < 1:
        user_menu_choice = int(input("Enter a positive integer between 1 and 3: "))
    return user_menu_choice

def readIn_paswd_string(): # Reads the password as a string
    password = input("Enter 8-digit password: ")
    return password


def main():
    encPass = None
    while True:
        print_menu()
        user_menu_choice = user_input_validation(readIn_user_input())
        if user_menu_choice == 1: # Will Encode the password
            encPass = encode(readIn_paswd_string())
            print()
        elif user_menu_choice == 3: # Will Exit the program
            exit()
        elif user_menu_choice == 2: # Will Decode the password
            if encPass == None:
                print("No Pass Encoded :(")
            else:
                decode(encPass)
        else:
            print("Oops somethinf went wrong, the program is terminating.")
            exit()


if __name__ == '__main__':
    main()