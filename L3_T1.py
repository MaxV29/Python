def div(a, b):
    try:
        a, b = float(a), float(b)
        div = a / b
    except ValueError:
        return "Введите число!"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return div

print(div(input("Введите первое число: "), input("Введите второе число: ")))