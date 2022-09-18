# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


def generate(numRows):
    matrix = []
    if numRows >= 1:
        matrix.append([1])
    if numRows >= 2:
        matrix.append([1,1])

    for i in range(3, numRows+1):
        array = []
        for j in range(i):
            if j == 0 or j == i-1:
                array.append(1)
            else:
                array.append(matrix[i-2][j-1]+matrix[i-2][j])
        matrix.append(array)
    return matrix

print(generate(6))



