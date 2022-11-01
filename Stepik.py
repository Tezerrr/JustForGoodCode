import numpy as np

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param second: list of "size" lists, each contains "size" floats
    """
    #YOUR CODE: please do not use numpy
    result = []
    size= len(first)
    for i in range(size):
        prom1=[]
        for j in range(size):
            a=0
            for k in range(size):
                a+= first[i][k]*second[k][j]
            prom1.append(a)
        result.append(prom1)
    return result
print(no_numpy_mult(
    [[1,2,3],
     [4,5,6],
     [7,8,9]],
    [[1,2,3],
     [4,5,6],
     [7,8,9]]))
def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """

    #YOUR CODE: please use numpy

    result =0 #YOUR CODE: create np.array
    return result