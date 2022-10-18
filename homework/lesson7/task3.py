"""A simple calculator.

Create a function called make_operation, which takes in a
simple arithmetic operator as a first parameter
(to keep things simple let it only be '+', '-' or '*')
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return 30
the call make_operation('*', 7, 6) should return 42

"""

def make_operation(operator, *args):


    #sum_1 = var1 + var2
    #sub_1 = var1 - var2
    #multi_1 = var1 * var2


    if operator == '+':
        sum_1 = sum(args)
        return sum_1
    elif operator == '-':
        sub_1 = args[0]
        for arg in args[1:]:
            sub_1 -= arg
        return sub_1
    elif operator == '*':
        multi_1 = 1
        for arg in args:
            multi_1 *= arg
        return multi_1
    else:
        print("Only +, - or * pls")
make_operation("+", 5, 6, 7, 9, 8)

print(make_operation("*", 5, 5, 5, 5, 5))
