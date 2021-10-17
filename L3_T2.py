def user_data (name, surname, birth, city, email, tel):
    print(f"{name.title()}, {surname.title()}, {birth}, {city.title()}, {email}, {tel}")
    return user_data

user_data (input("Введите ваше имя: "), input("Введите вашу фамилию: "), input("Введите вашу дату рождения: "), input("Введите ваш город: "), input("Введите ваш e-mail: "), input("Введите ваш телефон: "))