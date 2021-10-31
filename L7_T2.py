class Textil:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_sq_c(self):
        return self.w / 6.5 + 0.5

    def get_sq_j(self):
        return self.h * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f"Общая площадь ткани: \n"
                   f" {(self.w / 6.5 + 0.5) + (self.h * 2 + 0.3)}")

class Coat(Textil):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.sq_c = round(self.w / 6.5 + 0.5)

    def __str__(self):
        return f"Площадь на пальто: {self.sq_c}"

class Jacket(Textil):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.sq_j = round(self.h * 2 + 0.3)

    def __str__(self):
        return f"Площадь на костюм: {self.sq_j}"

coat = Coat(3, 7)
jacket = Jacket(2, 5)
print(coat)
print(coat.get_sq_full)
print(coat.get_sq_c())
print(jacket)
print(jacket.get_sq_full)
print(jacket.get_sq_j())