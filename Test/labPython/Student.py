import random


class Student:
    def __init__(self, name, surname, progres):
        self.__name = name
        self.__surname = surname
        self.__progress = progres

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name=''):
        if name.isalpha():
            self.__name = name
        else:
            print("Недопустимий формат імені")

    @property
    def surname(self):
        return self.__name

    @surname.setter
    def surname(self, surname=''):
        if surname.isalpha():
            self.__name = surname
        else:
            print("Недопустимий формат прізвища")

    def __repr__(self):

        return '({p1}, {p2}, {progress})'.format(p1=self.__name, p2=self.__surname, progress=self.__progress)

    def __str__(self):
        return self.__repr__()

    def gpa_semester(self, number_semester):
        if number_semester not in self.__progress:
            return "error"
        else:
            for i in self.__progress:
                if i == number_semester:
                    return sum(self.__progress[i]) / len(self.__progress[i])

    def gpa_for_all_years(self):
        sum_all_years = 0
        for i in self.__progress:
            sum_all_years += sum(self.__progress[i]) / len(self.__progress[i])
        return sum_all_years / len(self.__progress)

    def gpa_max(self):
        return max([sum(self.__progress[i]) / len(self.__progress[i]) for i in self.__progress])

    def gpa_min(self):
        return min([sum(self.__progress[i]) / len(self.__progress[i]) for i in self.__progress])


progress = {"Semester" + str(i): [random.randint(50, 100) for j in range(10)] for i in range(5)}
studentA = Student('Ivan', 'Popuk', progress)
print(studentA)
print(studentA.gpa_semester('Semester1'))
print(studentA.gpa_for_all_years())
print(studentA.gpa_max())
print(studentA.gpa_min())
