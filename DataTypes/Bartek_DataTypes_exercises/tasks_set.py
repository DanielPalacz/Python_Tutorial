# set

items = set(["one", "one", "noone", "one", "two", "three", 1, 2, 3])

# 1. Print the length of the set
# 2. Insert "one" to the set
# 3. Print the set 4 times. Is it the always same?
# 4. Pop an element. Which one got popped?
# 5. Remove any element.
# 6. How many elements are there?


A = set([1, 2, 3])
B = set([3, 1, 2])


# Compare A and B
print(A - B)
print(bool(A))
print(bool(A - B))
# Join A and B
A.union(B)
