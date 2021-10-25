def sumNum():
    try:
        with open("my_file5.txt", "w+") as f_obj:
            num = input("Введите набор цифр через пробел: \n")
            f_obj.writelines(num)
            my_num = num.split()

            print(sum(map(int, my_num)))
    except IOError:
        print("Ошибка в файле")
    except ValueError:
        print("Ошибка! Неправильный набор")
sumNum()