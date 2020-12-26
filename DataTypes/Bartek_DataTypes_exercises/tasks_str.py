# String: str, a string of characters
#

s = "this is a string"

# 1. Write the code that:
#    a) prints the length of string s
#    b) prints the first character of s
#    c) prints the last character of s
print(s[-1])
#    d) prints the first 5 characters of s
print(s[0:5:1])
#    e) prints the last 5 characters of s
print(s[-5::])
#    f) prints the first 5 characters of s backwards
print(s[4::-1])
#    e) prints the last 5 characters of s backwards
print(s[:-6:-1])

# 2. Write the code that:
#    a) prints s in uppercase ("THIS IS A STRING")
print(s.swapcase())
#    b) prints s capitalized ("This is a string")
print(s.capitalize())
#    c) prints s as title ("This Is A String")
print(s.title())


# 3. Write the code that:
#    a) counts all the letters "i" in s
print(s.count("i"))
#    b) counts all the letters "s" in s
print(s.count("s"))

print("---------------------------------------------------------------------------------------------------------")
s2 = "   \n this\tis\va\nstring\n"

# 4. Write the code that:
#    a) prints s2
print("start__ '", s2, "'__end", sep="")
#    b) counts the lines in s2
print(s2.count("\n"))
#    c) removes the leading whitespace
print("---------------------------------------------------------------------------------------------------------")
print(s2.lstrip())
print("---------------------------------------------------------------------------------------------------------")
#    d) removes the trailing whitespace
print("---------------------------------------------------------------------------------------------------------")
print(s2.rstrip())
print("---------------------------------------------------------------------------------------------------------")
#    e) strips whitespace from left and right
print("---------------------------------------------------------------------------------------------------------")
print(s2.strip())
s2_stripped = s2.strip()
print("---------------------------------------------------------------------------------------------------------")
print(f"{s2!r}")
#   f)
row_s2 = repr(s2)
print(row_s2)
table1 = [c for c in row_s2 if not c.isspace() if c != "'"]
print(table1)
table2 = [c for c in s2_stripped if not c.isspace() if c != "'"]
print(table2)


s3 = "الْحُرُوف الْعَرَبِيَّة"

# 5. Write the code that:
#    a) checks if s3 starts with "ة"
#    b) checks if s3 ends with "الْحُرُ"
if s3[-1] == "الْحُرُ":
    print("5b positively tested")
else:
    print("5b negatively tested")
#    c) prints 6th character of s3
#    d) prints 5th character of s3
#    e) prints 4th character of s3

# 6. Which methods of a str type modify the string, and which return a copy of the string transformed?
# answer:
# str is immutable!


# 7. str split/join method
# s = "this is a string"
s_spplitted = s.split(" ")
print(s_spplitted)
print(" ... ".join(s_spplitted))
print(" ".join(s_spplitted))

sx = "Hi hi. I m sx. i have 0 years 0 months."
print(sx.split("."))
sx_splitted = sx.split(".")
print(".".join(sx_splitted))
