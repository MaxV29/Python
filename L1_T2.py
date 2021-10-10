time = int(input("Введите время в секундах: "));
hour = int(time / 3600); # количество секунд
resSec = time % 3600; # остаток
minute = int(resSec / 60);
sec = resSec % 60;

print(f"{hour:02}:{minute:02}:{sec:02}");