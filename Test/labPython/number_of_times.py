# можливо код не надто читабельний проте працює добре і компактний
text = list(''.join(input().strip().lower().split()))
print([i for i in set(text) if text.count(i) == max([text.count(j) for j in set(text)])])
