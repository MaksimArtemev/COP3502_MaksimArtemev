# Written by Artemev Maksim Alexandrovich

def encode(password):
    # Check if the password is 8 digits long and contains only integers
    if len(password) != 8 or not password.isdigit():
        raise ValueError("Password should be an 8-digit string containing only integers")

    # Encode the password by shifting each digit up by 3 numbers
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)

    return encoded_password

def print_menu():
    print("Menu\n----------\n1. Encoder\n2. Decoder\n3. Exit\n")

def readIn_user_input():
    user_input = int(input("Enter 1 or 2: "))
    return user_input

def user_input_validation(user_menu_choice):
    while 3 < user_menu_choice < 1:
        user_menu_choice = int(input("Enter a positive integer between 1 and 3: "))
    return user_menu_choice

def readIn_paswd_string():
    password = input("Enter 8-digit password: ")
    return password


def decode(password):  # decodes an encoded password
    decoded = ''
    for digit in password:
        new_part = (int(digit) - 3) % 10
        decoded += str(new_part)
    return decoded


def main():
    storage = None
    while True:
        print_menu()
        user_menu_choice = user_input_validation(readIn_user_input())
        if user_menu_choice == 1:
            storage = encode(readIn_paswd_string())
            print(f"Encoded password: {storage}")
            print()
            continue
        elif user_menu_choice == 3:
            exit()
        elif user_menu_choice == 2:
            original = decode(storage)
            print(f"The encoded password is {storage}, and the original password is {original}.")
            continue
        else:
            print("Oops something went wrong, the program is terminating.")
            exit()


if __name__ == '__main__':
    main()