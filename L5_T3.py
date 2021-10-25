with open("my_file3.txt", "r") as my_file:
    sal = []
    cool = []
    my_list = my_file.read().split("\n")
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            cool.append(i[0])
        sal.append(i[1])
print(f"Оклад меньше 20000 {cool}, средний оклад {sum(map(int, sal)) / len(sal)}")