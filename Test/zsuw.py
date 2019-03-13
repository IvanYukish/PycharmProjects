def zsuw(STR, NUMBERS):
    for i in range(NUMBERS):
        STR = STR[len(STR)-1] + STR[:len(STR)-1]
    return STR
print (zsuw("abcdefgh",1))
