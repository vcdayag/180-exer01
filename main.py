import random
import time


# create a 2d list as a matrix
def generateMatrix(n: int) -> list[list[float]]:
    # generate a matrix with starting values of 0
    matrix = [[0 for y in range(n)] for x in range(n)]

    # randomly generate a value from 1 to 1000 for points with index divisible by 10
    for x in range(n // 10 + 1):
        for y in range(n // 10 + 1):
            # matrix[x * 10][y * 10] = random.randint(1, 1000)
            matrix[x * 10][y * 10] = 65+x+y

    return matrix


# Interpolate the given matrix
def terrain_inter(
    M: list[list[float]], n: int, rowBounds: tuple
) -> list[list[float]]:
    weights = ((0, 0, 0, 100), (0, 0, 10, 90), (0, 0, 20, 80), (0, 0, 30, 70), (0, 0, 40, 60), (0, 0, 50, 50), (0, 0, 60, 40), (0, 0, 70, 30), (0, 0, 80, 20), (0, 0, 90, 10), (0, 0, 100, 0), (0, 10, 0, 90), (1, 9, 9, 81), (2, 8, 18, 72), (3, 7, 27, 63), (4, 6, 36, 54), (5, 5, 45, 45), (6, 4, 54, 36), (7, 3, 63, 27), (8, 2, 72, 18), (9, 1, 81, 9), (10, 0, 90, 0), (0, 20, 0, 80), (2, 18, 8, 72), (4, 16, 16, 64), (6, 14, 24, 56), (8, 12, 32, 48), (10, 10, 40, 40), (12, 8, 48, 32), (14, 6, 56, 24), (16, 4, 64, 16), (18, 2, 72, 8), (20, 0, 80, 0), (0, 30, 0, 70), (3, 27, 7, 63), (6, 24, 14, 56), (9, 21, 21, 49), (12, 18, 28, 42), (15, 15, 35, 35), (18, 12, 42, 28), (21, 9, 49, 21), (24, 6, 56, 14), (27, 3, 63, 7), (30, 0, 70, 0), (0, 40, 0, 60), (4, 36, 6, 54), (8, 32, 12, 48), (12, 28, 18, 42), (16, 24, 24, 36), (20, 20, 30, 30), (24, 16, 36, 24), (28, 12, 42, 18), (32, 8, 48, 12), (36, 4, 54, 6), (40, 0, 60, 0), (0, 50, 0, 50), (5, 45, 5, 45), (10, 40, 10, 40), (15, 35, 15, 35), (20, 30, 20, 30), (25, 25, 25, 25), (30, 20, 30, 20), (35, 15, 35, 15), (40, 10, 40, 10), (45, 5, 45, 5), (50, 0, 50, 0), (0, 60, 0, 40), (6, 54, 4, 36), (12, 48, 8, 32), (18, 42, 12, 28), (24, 36, 16, 24), (30, 30, 20, 20), (36, 24, 24, 16), (42, 18, 28, 12), (48, 12, 32, 8), (54, 6, 36, 4), (60, 0, 40, 0), (0, 70, 0, 30), (7, 63, 3, 27), (14, 56, 6, 24), (21, 49, 9, 21), (28, 42, 12, 18), (35, 35, 15, 15), (42, 28, 18, 12), (49, 21, 21, 9), (56, 14, 24, 6), (63, 7, 27, 3), (70, 0, 30, 0), (0, 80, 0, 20), (8, 72, 2, 18), (16, 64, 4, 16), (24, 56, 6, 14), (32, 48, 8, 12), (40, 40, 10, 10), (48, 32, 12, 8), (56, 24, 14, 6), (64, 16, 16, 4), (72, 8, 18, 2), (80, 0, 20, 0), (0, 90, 0, 10), (9, 81, 1, 9), (18, 72, 2, 8), (27, 63, 3, 7), (36, 54, 4, 6), (45, 45, 5, 5), (54, 36, 6, 4), (63, 27, 7, 3), (72, 18, 8, 2), (81, 9, 9, 1), (90, 0, 10, 0), (0, 100, 0, 0), (10, 90, 0, 0), (20, 80, 0, 0), (30, 70, 0, 0), (40, 60, 0, 0), (50, 50, 0, 0), (60, 40, 0, 0), (70, 30, 0, 0), (80, 20, 0, 0), (90, 10, 0, 0), (100, 0, 0, 0))
    for row in range(*rowBounds):
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
                
                if row % 10 == 0:
                    continue

            # get the weighted area of the lower resolution points
            index = row % 10 + col % 10
            # top left
            d = weights[index][0]
            # top right
            c = weights[index][1]
            # bottom left
            b = weights[index][2]
            # bottom right
            a = weights[index][3]

            # get the values of the lower resolution points
            A = M[LRPOINTrow][LRPOINTcol]
            B = M[LRPOINTrow][LRPOINTcol + 10]
            C = M[LRPOINTrow + 10][LRPOINTcol]
            D = M[LRPOINTrow + 10][LRPOINTcol + 10]

            # get interpolation using Area Weighted Interpolation
            M[row][col] = (a * A + b * B + c * C + d * D) / 100
    return M


def generateSubmatrices(M: list[list[float]], n: int, t: int):
    submatrices = []
    rangeRow = (n // 10) // t
    # print(len(M))
    # print(rangeRow)
    for threads in range(t):
        onematrix = []
        lowwerbound = (threads * rangeRow) * 10
        upperbound = lowwerbound + (rangeRow * 10) + 1
        # print("lower, upper",lowwerbound, upperbound)
        for row in range(lowwerbound, upperbound):
            onematrix.append(M[row][:])
        submatrices.append(onematrix[:])
        # print(len(onematrix))

    return submatrices


from concurrent.futures import ThreadPoolExecutor, as_completed


def mulithreading(submatrices, n, t):
    with ThreadPoolExecutor(max_workers=t) as executor:
        rangeRow = (n // 10) // t
        lowwerbound = 0
        upperbound = lowwerbound + (rangeRow * 10) + 1

        args = [(submatrix, n, (lowwerbound, upperbound)) for submatrix in submatrices]
        futures = []
        
        for i in executor.map(lambda p:terrain_inter(*p),args):
            futures.append(i)

        output = []
        for idx, threadGenerated in enumerate(futures):
            if idx != 0:
                threadGenerated.pop(0)
            for x in threadGenerated:
                print(x)
            output.extend(threadGenerated)
        return output


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1]) + 1
    # number of threads
    t = int(sys.argv[2])

    M = generateMatrix(n)

    submatrices = generateSubmatrices(M, n, t)
    # for x in submatrices:
    #     for y in x:
    #         print(y)
    time_before = time.time()
    output = mulithreading(submatrices, n, t)
    time_after = time.time()

    time_elapsed = time_after - time_before

    # print(f"Time elapsed: {time_elapsed} seconds")

    # for x in output:
    #     print(x)
    
    
