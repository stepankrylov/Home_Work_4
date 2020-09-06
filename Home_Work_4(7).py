def fact(x_1, x_2):
    for n in range(x_1, x_2):
        factorial = 1
        for i in range(2, n+1):
            factorial *= i

        yield n, factorial


for item in fact(0, 10):
    print(f'Факториал числа {item[0]} равен {item[1]}')
