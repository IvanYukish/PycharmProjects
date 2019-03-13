from decimal import *
income = Decimal(input('Введіть місячний дохід - '))
podatok = income*Decimal(0.18)+income*Decimal(0.015)
print(podatok)