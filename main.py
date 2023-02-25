import random
import time


# create a 2d list as a matrix
def generateMatrix(n: int) -> list[list[float]]:
    # generate a matrix with starting values of 0
    matrix = [[0 for y in range(n)] for x in range(n)]

    # randomly generate a value from 1 to 1000 for points with index divisible by 10
    for x in range(n // 10 + 1):
        for y in range(n // 10 + 1):
            matrix[x * 10][y * 10] = random.randint(1, 1000)

    return matrix


# Area Weighted Interpolation
def awi(M, row, col) -> float:
    incrementrow = 10
    incrementcol = 10

    # get the coordinates of the nearest lower resolution point
    LRPOINTrow = row // 10 * 10
    LRPOINTcol = col // 10 * 10

    # check if the resolution point is the top left
    # if not update the LRPOINTrow or LRPOINTcol accordingly

    if row % 10 == 0 and row != 0:
        LRPOINTrow -= 10
    if col % 10 == 0 and col != 0:
        LRPOINTcol -= 10

    # get the weighted area of the lower resolution points

    # top left
    d = (row - LRPOINTrow) * (col - LRPOINTcol)
    # top right
    c = (row - LRPOINTrow) * (LRPOINTcol + incrementcol - col)
    # bottom left
    b = (LRPOINTrow + incrementrow - row) * (col - LRPOINTcol)
    # bottom right
    a = (LRPOINTrow + incrementrow - row) * (LRPOINTcol + incrementcol - col)

    # get the values of the lower resolution points

    A = M[LRPOINTrow][LRPOINTcol]
    B = M[LRPOINTrow][LRPOINTcol + incrementcol]
    C = M[LRPOINTrow + incrementrow][LRPOINTcol]
    D = M[LRPOINTrow + incrementrow][LRPOINTcol + incrementcol]

    return (a * A + b * B + c * C + d * D) / (a + b + c + d)


# Interpolate the given matrix
def terrain_inter(M: list[list[float]], n: int):
    for row in range(n):
        for col in range(n):
            M[row][col] = awi(M, row, col)
    return M


if __name__ == "__main__":
    n = int(input("value of n: ")) + 1
    M = generateMatrix(n)

    time_before = time.time()
    output = terrain_inter(M, n)
    time_after = time.time()

    time_elapsed = time_after - time_before

    print(f"Time elapsed: {time_elapsed} seconds")
