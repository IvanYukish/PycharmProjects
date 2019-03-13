n = list(map(int, list(input())))
print('Счастливый' if sum(n[:3]) == sum(n[3:]) else 'Обычный')