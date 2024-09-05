import re
import secrets
import string
import sys


def generate_password(length, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password


arguments = sys.argv

if len(arguments) < 3:
    print('Missing arguments, argument "--length" and its value must be inserted ')
    sys.exit(1)

if arguments[1] != '--length':
    print('Argument "--length" or value of the length is required as input for the script')
else:
    new_password = generate_password(int(arguments[2]))

if len(arguments) == 5:
    if arguments[3] == '--nums':
        new_password = generate_password(int(arguments[2]), int(arguments[4]))
elif len(arguments) == 7:
    if arguments[5] == '--special_chars':
        new_password = generate_password(int(arguments[2]), int(arguments[6]))
elif len(arguments) == 9:
    if arguments[7] == '--uppercase':
        new_password = generate_password(int(arguments[2]), int(arguments[8]))
elif len(arguments) == 11:
    if arguments[9] == '--lowercase':
        new_password = generate_password(int(arguments[2]), int(arguments[10]))

if len(arguments) == 6 or len(arguments) == 8 or len(arguments) == 10 or len(arguments) == 12:
    print('Value missing, insert the value of the argument')

print('Generated password:', new_password)
