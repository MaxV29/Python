billing = int(input("Введите вашу прибыль: "));
cost = int(input("Введите издержки фирмы: "));

if billing > cost:
    rent = billing / (billing - cost) * 100
    print("Вы сработали в прибыль. Рентабельность выручки:", round(rent, 2), "%");
elif billing == cost:
    print("Вы сработали в ноль.");
else:
    print("Вы сработали в убыток");

workN = int(input("Введите количество сотрудников: "));
profitNWork = (billing - cost) / workN
print("Прибыль фирмы в расчете на одного сотрудника:", round(profitNWork,2), "руб.");