from time import sleep

class TrafficLight:
    __color = ["Красный", "Жёлтый", "Зелёный"]

    def running(self):
        i = 0
        while i < 3:
            print(f"Внимание! Светофор производит переключение: \n" 
                  f"{TrafficLight.__color[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()