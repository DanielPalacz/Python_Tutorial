
import sys
import os
#sys.path.append(os.path.dirname((os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
__name__ = "lala"
from ..package1.bubu import bubu_function


def lala_function():
    print(f"I am lala_function and next I will be running bubu_function from package1.bubu")
    bubu_function()

print("lalallallalalalalalallalala")
print(dir())
print("sys.path content:")
for single_path in sys.path:
    print(single_path)
print("lalallallalalalalalallalala")

