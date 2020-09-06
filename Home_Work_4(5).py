from functools import reduce

x_1 = 100
x_2 = 1000
n = 2

res = reduce((lambda a, b: a * b), [i for i in range(x_1, x_2+1, n)])
print(res)
