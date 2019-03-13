def is_happy_ticket():
    Stroka = input()
    lstA = list(Stroka[:len(Stroka)//2:])
    lstB = list(Stroka[len(Stroka)-(len(lstA))::])
    if sum(lstA) == sum(lstB):
        return True
    else:
        return False


is_happy_ticket()