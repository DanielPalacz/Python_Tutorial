
# 1.
print()
print("1:", r"[elem**2 for elem in (range(1, 11))]")
list_c1 = [elem**2 for elem in (range(1, 11))]
print(list_c1, "\n")  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2.
print("2.1:", r"[elem for elem in (range(1, 11)) if elem % 3 != 0]")
list_c2 = [elem for elem in (range(1, 11)) if elem % 3 != 0]
print(list_c2, "\n")  # [1, 2, 4, 5, 7, 8, 10]

print("2.2:", r"[elem for elem in (range(1, 11)) if elem % 3 != 0 if elem % 2 ==1]")
list_c2 = [elem for elem in (range(1, 11)) if elem % 3 != 0 if elem % 2 == 1]
print(list_c2, "\n")

# 3.
list_a = [1, "", 3, 4]
list_b = [2, 3, 4, ""]

multiply_lista_listb1 = [a for a in list_a for b in list_b]
multiply_lista_listb2 = [(a, b) for a in list_a for b in list_b]
multiply_lista_listb3 = [(a, b) for a in list_a for b in list_b if bool(a) and bool(b)]
print("multiply_lista_listb1 = [a for a in list_a for b in list_b]")
print(multiply_lista_listb1)
print()
print("multiply_lista_listb2 = [(a, b) for a in list_a for b in list_b]")
print(multiply_lista_listb2)
print()
print("multiply_lista_listb3 = [(a, b) for a in list_a for b in list_b if bool(a) and bool(b)]")
print(multiply_lista_listb3)
print()

# 4
# chars = [c if c in used else "_" for c in secret]
print("""4. 
used = set(["k", "m"])
secret = ["k", "o", "t", "e", "k"]
chars1 = [c if c in used else "_" for c in secret]""")

used = set(["k", "t", "m"])
secret = ["k", "o", "t", "e", "k"]
chars1 = [c if c in used else "_" for c in secret]
print(chars1)
print()

# 5. Set comprehensions are doable
print("""5.
Set comprehensions are doable""")
s_comprehensed = {s for s in used if s != "t"}
print(s_comprehensed)
print(type(s_comprehensed))

# 6. Dictionary comprehensions are doable too
print("""
6.
Dictionary comprehensions are doable too""")
s1 = "ab;dwjkewfdjl;efw;ljkfewl;kefwkl;efw"
d1 = dict()
for i_val, single_str in enumerate(s1):
    d1[single_str] = i_val

d_comprehenced = {v: k for k, v in d1.items()}
print("d1 dictionary will be inverted by using dict comprehension: d_comprehenced = {v: k for k, v in d1.items()}")
print("d1:")
print(d1)
print("d_comprehenced:")
print(d_comprehenced)



