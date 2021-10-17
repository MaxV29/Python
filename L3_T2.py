def user_data (name, surname, birth, city, email, tel):
    print(f"{name.title()}, {surname.title()}, {birth}, {city.title()}, {email}, {tel}")
    return user_data

user_data (input("Введите имя: "), input("Введите фамилию: "), input("Введите дату рождения: "), input("Введите город: "), input("Введите e-mail: "), input("Введите телефон: "))