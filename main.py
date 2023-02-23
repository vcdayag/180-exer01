import random
import time

def generateMatrix(n:int) -> list[list[float]]:

    matrix = [ [0 for y in range(n)] for x in range(n)]

    for x in range(n//10+1):
        for y in range(n//10+1):
            matrix[x*10][y*10] = random.randint(1,1000)

    return matrix

# Area Weighted Interpolation
def awi(M,row,col) -> float:
    # index of the top left given point
    sectionrow = row//10
    sectioncol = col//10

    incrementrow = 10
    incrementcol = 10

    if sectionrow*10 == row and row != 0:
        incrementrow = 0
    if sectioncol*10 == col and col != 0:
        incrementcol = 0


    # top left
    d = abs(sectionrow-row)*abs(sectioncol-col)
    # top right
    c = abs(sectionrow-row)*abs(sectioncol+incrementcol-col)
    # bottom left
    b = abs(sectionrow+incrementrow-row)*abs(sectioncol-col)
    # bottom right
    a = abs(sectionrow+incrementrow-row)*abs(sectioncol+incrementcol-col)

    A = M[sectionrow][sectioncol]
    B = M[sectionrow][sectioncol+incrementcol]
    C = M[sectionrow+incrementrow][sectioncol]
    D = M[sectionrow+incrementrow][sectioncol+incrementcol]

    return (a*A + b*B + c*C + d*D) / (a+b+c+d)

def terrain_inter(M:list[list[float]],n:int):
    for row in range(n):
        for col in range(n):
            if row%10 == 0 and col%10 == 0:
                continue
            M[row][col] = awi(M, row, col)

if __name__ == "__main__":
    n = int(input("value of n: ")) + 1
    M = generateMatrix(n)
    print(M)

    time_before = time.time()
    terrain_inter(M,n)
    time_after = time.time()

    for x in M:
        print(x)

    time_elapsed = time_after - time_before

    print(f"Time elapsed: {time_elapsed} seconds")