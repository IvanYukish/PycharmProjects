# 1 і останнє слово
text = input().strip().split()
text[1:len(text) - 1] = []
text = ' '.join(text)
print(text)
