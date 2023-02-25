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

    matrix[0][0] = 200
    matrix[0][10] = 500
    matrix[10][0] = 50
    matrix[10][10] = 10

    return matrix


# Area Weighted Interpolation
def awi(M, row, col) -> float:
    # get the index of the top left lower resolution point

    sectionrow = row // 10
    sectioncol = col // 10

    incrementrow = 10
    incrementcol = 10

    if row % 10 == 0 and row != 0:
        sectionrow -= 1
    if col % 10 == 0 and col != 0:
        sectioncol -= 1

    sectioncol *= 10
    sectionrow *= 10

    # get the weighted area of the lower resolution points

    # top left
    d = (row - sectionrow) * (col - sectioncol)
    # top right
    c = (row - sectionrow) * (sectioncol + incrementcol - col)
    # bottom left
    b = (sectionrow + incrementrow - row) * (col - sectioncol)
    # bottom right
    a = (sectionrow + incrementrow - row) * (sectioncol + incrementcol - col)

    sectioncol //= 10
    sectionrow //= 10

    # get the values of the lower resolution points

    A = M[sectionrow][sectioncol]
    B = M[sectionrow][sectioncol + incrementcol]
    C = M[sectionrow + incrementrow][sectioncol]
    D = M[sectionrow + incrementrow][sectioncol + incrementcol]

    return (a * A + b * B + c * C + d * D) / (a + b + c + d)


# Interpolate the given matrix
def terrain_inter(M: list[list[float]], n: int):
    for row in range(n):
        for col in range(n):
            M[row][col] = awi(M, row, col)
    return M


if __name__ == "__main__":
    truevalue = [
        [200, 230.0, 260.0, 290.0, 320.0, 350.0, 380.0, 410.0, 440.0, 470.0, 500],
        [185.0, 211.6, 238.2, 264.8, 291.4, 318.0, 344.6, 371.2, 397.8, 424.4, 451.0],
        [170.0, 193.2, 216.4, 239.6, 262.8, 286.0, 309.2, 332.4, 355.6, 378.8, 402.0],
        [155.0, 174.8, 194.6, 214.4, 234.2, 254.0, 273.8, 293.6, 313.4, 333.2, 353.0],
        [140.0, 156.4, 172.8, 189.2, 205.6, 222.0, 238.4, 254.8, 271.2, 287.6, 304.0],
        [125.0, 138.0, 151.0, 164.0, 177.0, 190.0, 203.0, 216.0, 229.0, 242.0, 255.0],
        [110.0, 119.6, 129.2, 138.8, 148.4, 158.0, 167.6, 177.2, 186.8, 196.4, 206.0],
        [95.0, 101.2, 107.4, 113.6, 119.8, 126.0, 132.2, 138.4, 144.6, 150.8, 157.0],
        [80.0, 82.8, 85.6, 88.4, 91.2, 94.0, 96.8, 99.6, 102.4, 105.2, 108.0],
        [65.0, 64.4, 63.8, 63.2, 62.6, 62.0, 61.4, 60.8, 60.2, 59.6, 59.0],
        [50, 46.0, 42.0, 38.0, 34.0, 30.0, 26.0, 22.0, 18.0, 14.0, 10],
    ]
    # n = int(input("value of n: ")) + 1
    n = 11
    M = generateMatrix(n)

    time_before = time.time()
    output = terrain_inter(M, n)
    time_after = time.time()

    time_elapsed = time_after - time_before

    print(f"Time elapsed: {time_elapsed} seconds")

    print(truevalue == output)
