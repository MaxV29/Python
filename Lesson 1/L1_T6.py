a = int(input("1-й день: "))
b = int(input("Последний день: "))
n = 1
print(f'{n}-й день: {round(a, 2)} км.')

while a <= b:
  a = a + (a / 100 * 10)
  n += 1
  print(f'{n}-й день: {round(a, 2)} км.')