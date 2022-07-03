class Transpose:
    def solution_1(self, matrix):
        return [[matrix[x][y] for x in range(len(matrix))] for y in range(len(matrix[0]))]
