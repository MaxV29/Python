from sys import argv

script_name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f"Заработная плата сотрудника {res}")
except ValueError:
    print("Not a number")