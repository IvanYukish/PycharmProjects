lstA = [i for i in range(20)]
lstB = [i for i in lstA if i % 2 == 0]
text = ''.join('abdfbdfbthrh')
lstC = [i*3 for i in text]

print(lstB)
print(''.join(lstC))