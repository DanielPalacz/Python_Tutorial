import random

# Let's learn about list comprehensions!
# You are given 3 ints and represent the dimens of a cuboid along with an ints.
# Print a list of all possible coordinates given by on a 3D grid where the sum of  is not equal to n.
# Please use list comprehensions rather than multiple loops, as a learning

x = random.randint(0, 101)
y = random.randint(0, 101)
z = random.randint(0, 101)
n = random.randint(0, 101)

list_out = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k <= n]

for elem in list_out:
    print(elem)

print("x:", x, "y:", y, "z:", z, "n:", n)
