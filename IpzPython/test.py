# class Singleton:
#     _instance = None
#
#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#
# a = Singleton()
# b = Singleton()
# c = Singleton()
# print(id(a), id(b), id(c))
# print(a is b is c)
# class Student:
#     def __init__(self, first, last, rating:list):
#         self.first_name = first
#         self.lastname = last
#         self.rating = rating
#
#     def is_scholarship(self):
#         if sum(self.rating)/len(self.rating) > 50:
#             return True
#         else:
#             return False
#
# lst = [50,35,47,59,100]
# a = Student('vasa', 'pupkin', lst)
# print(a.is_scholarship())
# class Animals:
#     def move(self):
#         pass
#
#
# class cow(Animals):
#     def move(self):
#         return "I walk"
#
#
# class perch(Animals):
#     def move(self):
#         return "I swim"
#
#
# class cparrow(Animals):
#     def move(self):
#         return "I fly"
