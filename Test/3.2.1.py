def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif key not in d:
        if key * 2 not in d:
            d[key * 2] = [value]
        else:
            d[key * 2] += [value]


d = {}
update_dictionary(d, 1, -1)
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
