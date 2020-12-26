numbers = [1, 2, 3, 6, 5, 4, 7, 8, 9, 0]

## Assignments:
# 1. Print the list in ascending order, without modifying the list
print(sorted(numbers))
# 2. Print the list in descending order, without modifying the list
print(sorted(numbers, reverse=True))
# 3. Print the elements starting from the third one
print(numbers[2:])
# 4. Print the elements backwards starting from the last one
print(numbers[::-1])
# 5. Print the max element
print(max(numbers))
# 6. Print the min element
print(min(numbers))
# 7. Print the sum of all the elements
print(sum(numbers))
# 8. Print the sum of all even elements
print(sum([num for num in numbers if num % 2 == 0]))
# 9. Insert a number 6 at sixth position
print(numbers)
numbers[5] = 6
print(numbers)
# 10. Print the number of elements without counting duplicates twice
print(len(numbers))
print(len(set(numbers)))
# 11. Remove all even elements
numbers = [num for num in numbers if num % 2 == 1]
print(numbers)
# 13. Remove the last element
del numbers[-1]
print(numbers)
# 14. Print the last element
print(numbers[-1])
# 15. Add a list [8, 8] to the remaining list
numbers += [8, 8]
print(numbers)
# 16. Print the length of the list
print(len(numbers))
# 15. Extend the list with the following list [9, 9]
numbers.extend([9, 9])
print(numbers)


elements = ["wikipedia.org", "khanacademy.org", "matplotlib.org",
            "scipy.org", "google.com", "facebook.com", "twitter.com"]

# a) Remove "google.com"
print(elements)
elements.remove("google.com")
print(elements)
# b) Remove 4th element
del elements[3]
print(elements)
# c) Remove last element
del elements[-1]
print(elements)
# d) Print the second element
print(elements[1])
# e) Sort the list in-place
elements.sort()
print(elements)


things = [
    ["red", "blood", "sun"],
    ["green", "lime", "grass"],
    ["white", "clouds", "snow"],
    ["black", "hole", "gravity"],
    ["blue", "ocean", "planet"],
]

# a) Write the expression that indexes "planet"
# b) Write the expression that indexes "hole"
# c) Write the expression that indexes "white"
# d) Write the expression that indexes "grass"
# e) Write the expression that indexes "blood"
# f) Print the length of the list of things


numbers = [1, 2, 3, 4, 5, "one", {}, 6, 7, 1, 2, 3, 4, 5, 6, 7]


## Tasks:
# 1. Print the numeric elements of the list
print(numbers)
print([num for num in numbers if isinstance(num, int)])
# 2. Remove the non-numeric elements from the list
numbers = [num for num in numbers if isinstance(num, int)]
print(numbers)
# 3. Remove the duplicates from the list, or rewrite the list without duplicates
numbers = list(set(numbers))
print(numbers)
# 4. Make a list of all the elements squared
squared_numbers = [num*num for num in numbers]
print(squared_numbers)
# 5. Print the average of the list
avg = sum(squared_numbers)/len(squared_numbers)
print(avg)
# 6. Print the list of elements that are greater than the average
print([num for num in squared_numbers if num > avg])


elements = ["a", "b", "c", 1]

# Sort the list.
# print(sorted(elements))
# --> TypeError


A = [1, 2, 3]
B = [4, 5, 6]

# Add B to A.
C = A + B
print(C)

# sort number pairs by second element of the pair. Do not touch initial structure
number_pairs = [(1, 22), (2, 1), (3, 33), (6, 2), (5, 4), (4, 44), (7, 77), (8, 3), (9, 7), (0, 0)]
sorted_pairs = sorted(number_pairs, key=lambda pair: pair[1])
print(sorted_pairs)
