initial_list = input().split()
for element in set(initial_list):
    if initial_list.count(element) > 1:
        print(element, end=" ")

# s = input().split()
# print(*(i for i in set(s) if s.count(i) > 1))





