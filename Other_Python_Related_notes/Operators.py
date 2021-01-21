

# https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
# https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions


# Python ternary operator

# If used properly, ternary operator can reduce code size and increase readability of the code.
# No special keyword for ternary operator, it is if-else statement that creates a ternary statement / conditional expr.
# [when_true] if [condition] else [when_false]

is_slow = False
car = "Ferrari" if is_slow else "Sedan"
print(car)

#  ==

if is_slow:
    car = "Ferrari"
else:
    car = "Sedan"

# #####################################################################################


