# first, *rest, last = 1,2,3,4,5
# print(*rest)
# def funk(a, *b):
#
#     return list(b)
#
#
# print(funk(1,2,3,3,5,6,7,8,9))
#
# def ss(*args):
#     sett = {i for i in args}
#     lst = {i for i in sett}
#     return lst
#
# print(ss(1,2,3,4,5))
# print(ss(1,2,3,4,5))
#
# for a, *b in {range(1, 4), range(1, 5), range(1, 6)}:
#     print(b)
# def a ():
#     def b():
#         def c(x):
#             return x**2
#         return c
#     return b
#
# f = a()
# D = f()
# print(D(3))
#
# mib = 42
# print(globals())


def make_min(*, lo, hi):
    def inner(first, *ards):
        res = hi
        for arg in (first,) + ards:
            if arg < res and lo < arg < hi:
                res = arg
        return max(res, lo)

    return inner


bounded_min = make_min(lo=14, hi=25)
print(bounded_min(-5, 12, 13))
