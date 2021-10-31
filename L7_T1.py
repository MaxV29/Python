class Matrix:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def __add__(self):
        matx = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        for i in range(len(self.l1)):
            for n in range(len(self.l2[i])):
                matx[i][n] = self.l1[i][n] + self.l2[i][n]
        return str("\n".join(["\t".join([str(n) for n in i]) for i in matx]))

        def __str__(self):
            return str("\n".join(["\t".join([str(n) for n in i]) for i in matx]))

my_matrix = Matrix([[4, 20, 15],
                   [3, 21, 17],
                   [54, 49, 8]],
                   [[48, 5, 1],
                    [4, 20, 99],
                    [22, 4, 68]])

print(my_matrix.__add__())

