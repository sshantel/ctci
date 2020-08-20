"""
Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to 0.
"""


def zero_matrix(the_array, m, n):
    res = []
    i = 0
    for index, element in enumerate(the_array):
        for i in range(len(the_array)):
            if the_array[i] == 0:
                i += 1
        res.append(element)
    return res


print(zero_matrix([[0, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3))
