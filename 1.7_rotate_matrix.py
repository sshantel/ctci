"""
Given an image represented by an NxN matrix, where each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
"""


def rotate_matrix(the_array):
    res = []
    for i in range(len(the_array)):
        print(i)
        transposed = []
        for col in the_array:
            print(col[i])
            transposed.append(col[i])
        transposed.reverse()
        res.append(transposed)
    return res


print(rotate_matrix([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]))
