exec('''
def s1(a, b, c):
  p = (a + b + c) / 2
  return float( ( p * (p - a) * (p - b) * (p - c) ) ** (1 / 2) )

figure = {'треугольник': [3, lambda a, b, c: s1(a, b, c)], 
          'прямоугольник': [2, lambda a, b: a * b], 
          'круг': [1, lambda r: 3.14 * r**2 ]}
f = str(input())
print(figure[f][1](*(float(input()) for _ in range(figure[f][0]))))
''')