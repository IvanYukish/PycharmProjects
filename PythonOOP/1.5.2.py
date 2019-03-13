class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        [self.lst.append(i) for i in a]
        sum = 0
        for j, i in enumerate(self.lst):
            if j % 5 == 0 and j != 0:
                print(sum)
                sum = 0
            sum += i
        if len(self.lst) % 5 == 0 and len(self.lst) != 0:
            print(sum)
            sum = 0
        self.lst = self.lst[len(self.lst) - len(self.lst) % 5::]

    def get_current_part(self):
        return self.lst


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]

