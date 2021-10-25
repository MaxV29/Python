my_f = open("my_file.txt", "w")
f = input("Введите данные: \n")
while True:
    my_f.writelines(f)
    f = input("Введите данные: \n")
    if not f:
        break

my_f.close()
my_f = open("my_file.txt", "r")
data = my_f.readlines()
print(data)
my_f.close()