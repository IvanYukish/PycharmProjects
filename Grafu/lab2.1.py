# пошук в ширину
from collections import deque

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['alice'] = ['peggy']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
search_queue = deque()

search_queue += graph['you']


def person_is_seller(name):
    return name[-1] == 'm'

print(graph)
while search_queue:
    print(search_queue)
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + ' - продавець морозива')
        break
    else:
        search_queue += graph[person]

print(graph)
print(search_queue)
