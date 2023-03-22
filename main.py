# angel peter
def encode(password):
    encoded_string = ""
    encode_dict = {"0": "3","1": "4", "2": "5", "3": "6","4": "7",
                "5": "8", "6": "9", "7": "0", "8": "1", "9": "2"}
    for i in password:
        encoded_string += encode_dict[i]
    return encoded_string


def decode(new_password):
    orig_password = ''
    for digit in new_password:
        if digit == '0':
            orig_digit = 7
        elif digit == '1':
            orig_digit = 8
        elif digit == '2':
            orig_digit = 9
        else:
            orig_digit = int(digit) - 3
        orig_password += str(orig_digit)
    return orig_password


if __name__ == '__main__':
    keep_going = True
    while keep_going:
        print("\nMenu \n------------- \n1. Encode \n2. Decode \n3. Quit")
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            original_password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = encode(original_password)
        elif option == 2:
            original_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        elif option == 3:
            keep_going = False








