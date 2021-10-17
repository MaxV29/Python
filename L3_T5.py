sumPow = 0
while True:
    sNum = input('Введите числа через пробел: ')
    if sNum == 'q':
        break
    parts = sNum.split()
    for part in parts:
        sumPow += int(part)
    print(sumPow)

print(sumPow)