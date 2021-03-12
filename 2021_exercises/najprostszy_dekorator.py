import time
import functools


def timeit(decorated_function):
    @functools.wraps(decorated_function)
    def redefined(*args, **kwargs):

        t1 = time.monotonic()
        res = decorated_function(*args, **kwargs)
        t_delta = time.monotonic() - t1
        print(decorated_function, decorated_function.__doc__, t_delta)
        return res

    return redefined


@timeit
def hello(name, x, y, z):
    """hello initial docstring"""
    print("hello", name)
    return "17"


@timeit
def hello2():
    """hello2 initial docstring"""
    print("hello W")


help(hello)
hello("Jan", 1, 2, 3)
hello2()
