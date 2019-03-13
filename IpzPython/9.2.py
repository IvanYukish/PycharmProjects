from num2words import num2words

Number = float(input())


def converter(X, Drib):
    if 5 <= (X % 10) <= 9 or 11 <= (X % 100) <= 19 or X % 10 == 0:
        if Drib:
            return "Копійок"
        else:
            return "Гривень"
    elif 2 <= (X % 10) <= 4:
        if Drib:
            return "Копійки"
        else:
            return "Гривні"
    else:
        if Drib:
            return "Копійка"
        else:
            return "Гривня"


print(num2words(int(Number), lang='uk'), converter(int(Number) % 100, False), int(((Number % 1) * 100)+0.5),
      converter((Number%1)*100, True))
# from num2words import num2words
# print(num2words(12345.56, lang='uk', to='currency', currency='UAH'))
