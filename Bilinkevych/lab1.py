def count_symbols(word):
    if type(word) == str:
        return False
    Dictionary = {i: list(str(word)).count(i) for i in set(str(word))}
    return Dictionary


print(count_symbols('100500'))
print(count_symbols(100500))
