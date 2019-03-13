string = input()
num = 1
it = ""
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        num += 1
    else:
        it += string[i]+str(num)
        num = 1
print(it + num + str(num))
