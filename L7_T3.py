class Cell:
    def __init__(self, q):
        self.q = int(q)

    def __str__(self):
        return f'Результат операции {self.q * "*"}'

    def __add__(self, other):
        return Cell(self.q + other.q)

    def __sub__(self, other):
        return self.q - other.q if (self.q - other.q) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.q * other.q))

    def __truediv__(self, other):
        return Cell(round(self.q // other.q))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.q / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.q % cells_in_row)}'
        return row

cells1 = Cell(12)
cells2 = Cell(3)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)