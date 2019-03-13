def loud_letters():
    count = [i for i in input() if i in 'aouiey']
    return len(count)


print(loud_letters())