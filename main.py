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


# Interpolate the given matrix
def terrain_inter(M: list[list[float]], n: int):
    for row in range(n):
        # get the coordinates of the nearest lower resolution point
        LRPOINTrow = row // 10 * 10
        # check if the resolution point is the top left
        # if not update the LRPOINTrow or LRPOINTcol accordingly
        if row % 10 == 0 and row != 0:
            LRPOINTrow -= 10
        for col in range(n):
            if col % 10 == 0:
                # get the coordinates of the nearest lower resolution point
                LRPOINTcol = col // 10 * 10
                # check if the resolution point is the top left
                # if not update the LRPOINTrow or LRPOINTcol accordingly         
                if col != 0:
                    LRPOINTcol -= 10

            # get the weighted area of the lower resolution points

            # top left
            d = (row - LRPOINTrow) * (col - LRPOINTcol)
            # top right
            c = (row - LRPOINTrow) * (LRPOINTcol + 10 - col)
            # bottom left
            b = (LRPOINTrow + 10 - row) * (col - LRPOINTcol)
            # bottom right
            a = (LRPOINTrow + 10 - row) * (LRPOINTcol + 10 - col)

            # get the values of the lower resolution points

            A = M[LRPOINTrow][LRPOINTcol]
            B = M[LRPOINTrow][LRPOINTcol + 10]
            C = M[LRPOINTrow + 10][LRPOINTcol]
            D = M[LRPOINTrow + 10][LRPOINTcol + 10]

            M[row][col] = (a * A + b * B + c * C + d * D) / 100
    return M


if __name__ == "__main__":
    n = int(input("value of n: ")) + 1
    M = generateMatrix(n)

    time_before = time.time()
    output = terrain_inter(M, n)
    time_after = time.time()

    time_elapsed = time_after - time_before

    print(f"Time elapsed: {time_elapsed} seconds")
