import sys
import simplelazy as sl

VARIABLE_DICT = {}  # We store user inputed variables here
ALLOWED_OPERATIONS = {"add", "multiply", "subtract"}


# split the input and use lower case
def parse(input_str):
    input_str = input_str.lower()
    words = input_str.split()
    return words


# Convert numbers in string format to float
def fix_float(line):
    if line[2].isnumeric():
        line[2] = float(line[2])
    return line


def unseen(key):
    return key not in VARIABLE_DICT


def check_input_dub(line):
    if not line[0] == "print":
        raise SyntaxError("Only print is valid for line with two inputs")


def check_input_triple(line):
    if not line[0].isalnum():
        raise ValueError(line[0], "not alphanumeric")

    if line[0].isnumeric():
        raise ValueError(line[0], "cant have numbers as variable name")

    if line[1] not in ALLOWED_OPERATIONS:
        raise ValueError(line[1], " not an allowed operation")

    if line[1] not in ALLOWED_OPERATIONS:
        raise ValueError(line[1], " not an allowed operation")


# Note that we have overloaded the +-* operations to have the same
# syntax as the input
def evaluate(first_variable, operation_string, second_argument):
    if operation_string == "add":
        first_variable + second_argument
    if operation_string == "subtract":
        first_variable - second_argument
    if operation_string == "multiply":
        first_variable * second_argument


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SyntaxError("No file to read specified")
    filename = sys.argv[1]
    f = open(filename, "r")

    for x in f:
        line = parse(x)
        if len(line) < 1 or len(line) > 3:
            raise SyntaxError("too many or too few arguments")
        if len(line) == 2:
            check_input_dub(line)
            var = VARIABLE_DICT[line[1]]
            var.print()
        if len(line) == 3:

            line = fix_float(line)
            check_input_triple(line)

            first_argument = line[0]
            operation_string = line[1]
            second_argument = line[2]

            # Handle first argument
            if unseen(first_argument):
                first_variable = sl.Variable(0)
                dict_item = {first_argument: first_variable}
                VARIABLE_DICT.update(dict_item)

            else:
                first_variable = VARIABLE_DICT[first_argument]

            # Handle second argument
            if unseen(second_argument):
                if not isinstance(second_argument, float):
                    second_argument = sl.Variable(0)
                    dict_item = {line[2]: second_argument}
                    VARIABLE_DICT.update(dict_item)

            else:
                if not isinstance(second_argument, float):
                    second_argument = VARIABLE_DICT[second_argument]

            # Evaluation and dictionary update
            evaluate(first_variable, operation_string, second_argument)
            dict_item = {first_argument: first_variable}
            VARIABLE_DICT.update(dict_item)
