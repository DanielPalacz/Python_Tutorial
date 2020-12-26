
from package2.kuku import k1
from package2.lala import lala_function
import sys

# package2.lala.lala_function()
print()
print("Global namespace:")
print(dir())
print()

print(k1)

print("sys.path content:")
for single_path in sys.path:
    print(single_path)
