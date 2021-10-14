n = int(input("Введите число: "));
max = 0

while True:
    maxN = n % 10
    if max < maxN:
        max = maxN
    if max >= maxN:
        n = n // 10
        if n == 0:
            break;

print(max)