class DivByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def div_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деленить на ноль нельзя!")


div = DivByNull(1, 100)
print(DivByNull.div_by_null(100, 0))
print(DivByNull.div_by_null(100, 0.1))
print(div.div_by_null(100, 0))