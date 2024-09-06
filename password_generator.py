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


script_arguments = sys.argv
# Remove first element of collection that usually is script
script_arguments.pop(0)

if "--length" not in script_arguments:
    print("[ERROR] Missing argument --start")
    sys.exit(1)

length_value_index = script_arguments.index("--length") + 1

if len(script_arguments) < (length_value_index + 1):
    print("[ERROR] Argument --length value not provided")
    sys.exit(1)

length_value = script_arguments[length_value_index]

nums_value = 1
special_chars_value = 1
uppercase_value = 1
lowercase_value = 1

if "--nums" in script_arguments:
    nums_value_index = script_arguments.index("--nums") + 1
    if len(script_arguments) < (nums_value_index + 1):
        print("[ERROR] Argument --nums value not provided")
        sys.exit(1)
    else:
        nums_value = script_arguments[nums_value_index]

if "--special_chars" in script_arguments:
    special_chars_value_index = script_arguments.index("--special_chars") + 1
    if len(script_arguments) < (special_chars_value_index + 1):
        print("[ERROR] Argument --special_chars value not provided")
        sys.exit(1)
    else:
        special_chars_value = script_arguments[special_chars_value_index]

if "--uppercase" in script_arguments:
    uppercase_value_index = script_arguments.index("--uppercase") + 1
    if len(script_arguments) < (uppercase_value_index + 1):
        print("[ERROR] Argument --uppercase value not provided")
        sys.exit(1)
    else:
        uppercase_value = script_arguments[uppercase_value_index]

if "--lowercase" in script_arguments:
    lowercase_value_index = script_arguments.index("--lowercase") + 1
    if len(script_arguments) < (lowercase_value_index + 1):
        print("[ERROR] Argument --lowercase value not provided")
        sys.exit(1)
    else:
        lowercase_value = script_arguments[lowercase_value_index]

new_password = generate_password(
    int(length_value),
    int(nums_value),
    int(special_chars_value),
    int(uppercase_value),
    int(lowercase_value)
)

print('Generated password:', new_password)
