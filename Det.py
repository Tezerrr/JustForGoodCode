def det(matrix):
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) \
               - (matrix[0][1] * matrix[1][0])
    else:
        summ = 0
        ch = 1
        for i in range(len(matrix)):
            matr = []
            for j in range(1, len(matrix)):
                matr1 = []
                for k in range(len(matrix)):
                    if i != k:
                        matr1.append(matrix[j][k])
                    else:
                        continue
                matr.append(matr1)
            summ += ch * matrix[0][i] * det(matr)
            ch *= -1
        return summ


print(det([[5, 2,1, 0], [2, -5, -6, 1], [3, -4, 3, -2], [-1, 4, -5, 6]]))
