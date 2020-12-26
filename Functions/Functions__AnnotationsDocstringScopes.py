
x = "this_is__x__global_variable"


def foo(x: str, y: str = "y_arg_variable") -> str:
    """Docstring for foo."""

    print("locals() inside foo:", locals())
    return x + "____" + y


print("locals() in global namespace:", locals())
print("globals() in global namespace:", globals())
print(foo.__doc__)
# Docstring for foo.
print(foo.__annotations__)
# {'x': <class 'str'>, 'y': <class 'str'>, 'return': <class 'str'>}

foo_out = foo("Abc")
print(foo_out)
