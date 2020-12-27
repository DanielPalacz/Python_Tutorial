
list1 = [1, 2, 3]

list2 = list(map(lambda x: x*2, list1))
print(list2)

a_list = [1, 2, 3, 4]
b_list = [5, 6, 7]
print(list(zip(a_list, b_list)))
# [(1, 5), (2, 6), (3, 7)]

c_list = [8, 9]
print(list(zip(a_list, b_list, c_list)))
# [(1, 5, 8), (2, 6, 9)]

filtered_list = list(filter(lambda x: x > 2, a_list))
print(filtered_list)
# [3, 4]

