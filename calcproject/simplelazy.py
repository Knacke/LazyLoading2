import copy as cp


class Variable:
    def __init__(self, value):
        self.value_function = lambda: value
        # we store or the value as a lambda function so that evaluation can be deferred

    def print(self):
        print(self.value_function())  # this is where we actually evaluate the function.

    # overloaded addition.
    # used to change behaviour: of self + other
    def __add__(self, other):
        value_function_copy = cp.deepcopy(self.value_function)

        if isinstance(other, float):
            other = Variable(other)
        self.value_function = lambda: value_function_copy() + other.value_function()

    def __sub__(self, other):
        value_function_copy = cp.deepcopy(self.value_function)

        if isinstance(other, float):
            other = Variable(other)
        self.value_function = lambda: value_function_copy() - other.value_function()

    def __mul__(self, other):
        value_function_copy = cp.deepcopy(self.value_function)

        if isinstance(other, float):
            other = Variable(other)
        self.value_function = lambda: value_function_copy() * other.value_function()
