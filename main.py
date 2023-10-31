def main():
    run = True
    while run == True:
        print("1. Encode\n2. Decode\n3.Quit")
        selection = input("Select an option")
        if selection == "1":
            password = input("Input password to encode:")
            encoded = encode_pass(password)
            print(f"The encoded password is:{encoded}")
        elif selection == "2":
            print(decode_pass(encoded))
        elif selection == "3":
            run = False


def encode_pass(password):
    output = 0
    for i in range(len(password)):
        output += ((int(password[i]) + 3) % 10) * (10 ** (len(password) - i - 1))
    return str(output)


def decode_pass(password):
    encodedPassword = ""
    for digit in password:
        digitShift = str((int(digit) - 3) % 10)
        encodedPassword += digitShift

    return encodedPassword



if __name__ == "__main__":
    main()

