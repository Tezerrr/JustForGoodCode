# matrix = [
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [9, 3, 4, 5, 6, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
#     [9, 8, 7, 6, 5, 4],
#     [1, 2, 3, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6],
# ]

f = open("C://Users/Tezer/Downloads/lab6_in.txt", mode="r")
a = f.readline()
n = f.readline()
matrix = [list(map(int, i[:-1].split())) for i in f.readlines()]
#matrix = [i[:-1] for i in f.readlines()]
print(matrix)
i = 0
matrix = matrix[::-1]
number = 0
check = False
while i < len(matrix) and check == False:
    j = 0
    check = True
    first = matrix[i][0]
    a_mean = 0
    lenght = 0
    while j < len(matrix[i]) - 1:
        if matrix[i][j] < matrix[i][j + 1]:
            check = False
        if matrix[i][j] < first:
            a_mean += matrix[i][j]
            lenght += 1
        j += 1
    if check == True:
        number = len(matrix) - (i)
    if lenght != 0:
        print("Среднее ариф: ",a_mean / lenght)
    i += 1
print("ans: ",number)
