def closest_mod_5(x):
    return int(*[x for x in range(x, x + 2) if x % 5 == 0])


data = [i for i in range(10) for y in range(20, 40)]
dic = {d['id']: d for d in data}.values()
print(dic)
print(*dic)

# def closest_mod_5(x):
#     return (x + 4) // 5 * 5

# # print(closest_mod_5(4))
# closest_mod_5(10)

closest_mod_5(0)

print((0 + 4) // 5 * 5)
