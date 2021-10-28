class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} движется"

    def stop(self):
        return f"{self.name} остановился"

    def turn_right(self):
        return f"{self.name} повернул направо"

    def turn_left(self):
        return f"{self.name} повернул налево"

    def show_speed(self):
        return f"Текущая скорость {self.name} - {self.speed} км/ч"

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость городского авто {self.name} - {self.speed} км/ч")
        if self.speed > 40:
            return f"Скорость {self.name} выше допустимой для городского авто"
        else:
            return f"Скорость {self.name} оптимальная для городского авто"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость рабочего авто {self.name} - {self.speed} км/ч")
        if self.speed > 60:
            return f"Скорость {self.name} выше допустимой для рабочего авто"

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} из полиций"
        else:
            return f"{self.name} не из полиций"

bmw = SportCar(250, "Черная", "BMW", False)
lada = TownCar(60, "Красная", "Lada", False)
skoda = WorkCar(90, "Белая", "Skoda", True)
mercedes = PoliceCar(150, "Бело-голубой", "Mercedes", True)
print(skoda.turn_left())
print(f"Когда {lada.turn_right()}, {bmw.stop()}")
print(f"{skoda.go()}. {skoda.show_speed()}")
print(f"{skoda.name} - {skoda.color}")
print(f"{bmw.name} полицейская машина? {bmw.is_police}")
print(f"{skoda.name} полицейская машина? {skoda.is_police}")
print(bmw.show_speed())
print(lada.show_speed())
print(mercedes.police())
print(mercedes.show_speed())