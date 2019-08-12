MINIMUM_LENGTH = 4


def main():
    password = get_password()
    password = print_asterisks(password)
    print('*' * len(password))


def get_password():
    password = input("Enter password with minimum of {} characters: ".format(MINIMUM_LENGTH))
    return password


def print_asterisks(password):
    while len(password) < MINIMUM_LENGTH:
        password = get_password()
    return password


main()