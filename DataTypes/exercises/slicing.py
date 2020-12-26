

s1 = "abcdefghijklmnoprstuvwy"

# print(len(s1))
# 23
# print(s1[22])
# y

# print(s1[:])
# print(s1[::])
# abcdefghijklmnoprstuvwy

# print(s1[::2])
# acegikmortvy

######################################################################
#
#   Python Slicing:
#   iterable[start:end:step]
#
#   start:  any int from [-(len(iterable)-1); len(iterable)-1]
#   end:    any int from [-(len(iterable)-1); len(iterable)-1]
#   step:   any not-zero int from [-(len(iterable)-1); len(iterable)-1]
#
######################################################################

# print(s1[:-1])
# print(s1[:22])
# abcdefghijklmnoprstuvw

# print(s1[-1::-1])
# print(s1[::-1])
# ywvutsrponmlkjihgfedcba

print(s1[::1])
