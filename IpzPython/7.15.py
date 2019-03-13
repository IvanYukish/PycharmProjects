import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "01234567890"
symbols = "!@#$%^&*()?"
pass_len = 8
password = random.sample(letters+numbers+symbols, pass_len)
print(''.join(password))