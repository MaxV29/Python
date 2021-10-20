def scr_1():
    num = int(input("Введите число: "))
    from itertools import islice
    from itertools import count

    for i in islice(count(num), 10):
        print(i)
scr_1()

def scr_2():
    list = [1, True, "список", 10.1]
    from itertools import islice
    from itertools import cycle

    for i in islice(cycle(list), 10):
        print(i)
scr_2()

