import time
import functools


def timeit(loops=1):
    def _timeit(decorated_function):
        @functools.wraps(decorated_function)
        def redefined(*args, **kwargs):

            t1 = time.monotonic()

            for i in range(loops):
                decorated_function(*args, **kwargs)

            t_delta = time.monotonic() - t1
            print(decorated_function, decorated_function.__doc__, t_delta)

        return redefined
    return _timeit



@timeit(loops=10000)
def hello2():
    """hello2 initial docstring"""
    print("hello W")


help(hello2)
