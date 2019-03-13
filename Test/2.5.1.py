initial_list = list(map(int, input().split()))
# sum_list = [initial_list[index - 1] + initial_list[index - len(initial_list) + 1] for index, element in enumerate(initial_list)]
# print(sum_list)
sum_list = []
for index, element in enumerate(initial_list):
    if len(initial_list) != 1:
        sum_list.append(initial_list[index - 1] + initial_list[index - len(initial_list) + 1])
        print(sum_list[index], end=" ")
    else:
        print(initial_list[0])
