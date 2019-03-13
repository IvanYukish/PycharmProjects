lst = input().split()


def average_value(lstA):
    return sum(lstA) / len(lstA)


def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0


print(median.__dir__())
print(median.__get__(lst))
