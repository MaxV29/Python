def subj():
    try:
        mydict = {}
        with open("my_file6.txt", encoding='utf-8') as f_obj:
            for line in f_obj:
                name, stats = line.split(':')
                clasSum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = clasSum
            print(f"{mydict}")
    except FileNotFoundError:
        return 'Файл не найден.'

subj()