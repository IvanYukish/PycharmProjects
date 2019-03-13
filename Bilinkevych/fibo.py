def lst_fib():
    a = int(input())
    lst = [i for i in range(1, a + 1)]
    print(lst)

    def fib(a):
        if n == 1 or n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)


lst_fib()
