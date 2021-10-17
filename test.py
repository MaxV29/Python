# Решение с помощью цикла
def my_func(x = 10, y = -2):
    a = 1
    for i in list(range(-y)):
        sum = -a * x
        a = -sum
    return sum

numPow = my_func()
print(numPow)