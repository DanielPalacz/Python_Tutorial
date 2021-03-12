import unittest

# junit - Java
#

# print(type(unittest))
# print(dir())


def divide(a, b):
    return a / b


def assert_raises(exc_type, callable, *args):
    e = None
    try:
        callable(*args)
    except Exception as e2:
        e = e2
    assert issubclass(e, Exception), "(Any) Exception was not raised"
    assert e is exc_type


params = [1, 0]
assert_raises(ZeroDivisionError, divide, 1, 0)
assert_raises(ZeroDivisionError, divide, *params)


# x, y, z = (1, 2, 3, 4, 5, 6)
# print(type(x))


class TestDivision(unittest.TestCase):

    def test_divide1by1(self):
        """..."""
        self.assertEqual(divide(1, 1), 1, "Dividing 1 by 1 failed")

    def test_divide1by0(self):
        """..."""
        # self.assertRaises(ZeroDivisionError, divide, 1, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

