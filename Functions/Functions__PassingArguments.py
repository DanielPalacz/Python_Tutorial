

def function1(a, b=1):
    print(a + b)


# a - required argument
# b - optional argument


# two positional arguments:
function1(1, 2)

# one positional argument (required):
function1(1)

# one positional argument (required) and then 1 keyword argument:
function1(1, b=2)

# one keyword argument (required):
function1(a=1)

# two keyword arguments:
function1(a=1, b=2)

# one keyword argument (required) and next positional argument:
# function1(a=1, 1)
# SyntaxError: positional argument follows keyword argument

print("------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------")


def function2(pos1, pos2, /, pos_or_kwd=0, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)


function2(1, 1, kwd1=1, kwd2=1)
function2(1, 1, 1, kwd1=1, kwd2=1)
function2(1, 1, pos_or_kwd=1, kwd1=1, kwd2=1)


# How you cant define functions?

# def function3(**kwargs, *, pos_param):
#    print(pos_param)
#    print(kwargs)
#

# however this is possible:
def function4(*args, kwarg1):
    print(args, kwarg1)


function4(*[1, 2, 3], kwarg1="kwarg1 test")
function4(*[1, 2, 3], "kwarg1 test")
