"""
Given an image represented by an NxN matrix, where each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
"""

n = 4


def rotate_matrix(matrix):
    for x in range(0, (n / 2)):
        for y in range(x, n - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n - 1 - x]
            matrix[y][n - 1 - x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = temp

    def display_matrix(matrix):
        for i in range(0, N):
            for j in range(0, N):
                print(mat[i][j], end=" ")


print(rotate_matrix(4))
print(display_matrix(4))
