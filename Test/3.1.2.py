def modify_list(listed):
    listed[:] = [x // 2 for x in listed if x % 2 != 1]


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)
