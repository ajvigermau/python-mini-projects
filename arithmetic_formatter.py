import sys


def arithmetic_arranger(problems, val=False):
    arranged_problems = ''
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    # list of all operations in str format
    operations = list(map(lambda x: x.split()[1], problems))
    if (operations.count('+') + operations.count('-')) != len(operations):
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems
    numbers = []  # list of all operands in str format
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda x: len(x) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    top_row = ''
    dashes = ''
    values = list(map(lambda x: eval(x), problems))
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_row = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += operations[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if val:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
    return arranged_problems


script_arguments = sys.argv

# Remove first element of collection that usually is script
script_arguments.pop(0)

if "--problems" not in script_arguments:
    print("[ERROR] Missing argument --problems")
    sys.exit(1)

problems_value_index = script_arguments.index("--problems") + 1

if len(script_arguments) < (problems_value_index + 1):
    print("[ERROR] Argument --problems value not provided")
    sys.exit(1)

problems_value = (script_arguments[problems_value_index]).split(';')

val_value = False
if "--val" in script_arguments:
    val_value_index = script_arguments.index("--val") + 1
    if len(script_arguments) < (val_value_index + 1):
        print("[ERROR] Argument --val value not provided")
        sys.exit(1)
    else:
        val_value = script_arguments[val_value_index]

arranger = arithmetic_arranger(problems_value, val_value)

print(arranger)


# Examples
# print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
# print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
