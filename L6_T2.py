class Road:
    __length = None
    __width = None
    weigth = None
    i = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weigth = 25
        self.i = 5
        intake = self.length * self.width * self.weigth * self.i / 1000
        print(f"Необходимо {intake} тонн для покрытия дороги асфальтом.")

road_to_village = Road(20000, 5)
road_to_village.intake()