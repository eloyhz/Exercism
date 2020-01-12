class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []

        # get a list of rows (string with numbers separated by spaces)
        r = matrix_string.split('\n')
        for s in r:
            # get a list of columns (numbers as strings)
            t = s.split()
            row = []
            for u in t:
                row.append(int(u))
            self.matrix.append(row)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        col = []
        for i in range(0, len(self.matrix)):
            col.append(self.matrix[i][index-1])
        return col
