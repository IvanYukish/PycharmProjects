import re


def Decoding():
    with open('3.4.1.txt') as inf:
        Stroka = inf.readline().strip()

    lstA = re.findall(r'\d+', Stroka)
    Stroka = ''.join([i for i in Stroka if not i.isdigit()])
    lstA = [Stroka[index] * int(lstA[index]) for index in range(len(lstA)) if index < len(lstA)]
    print("".join(lstA))


Decoding()
