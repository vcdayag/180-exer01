import random
import time

def generateMatrix(n:int) -> list[list[int]]:

    matrix = [ [0 for y in range(n)] for x in range(n)]

    for x in range(n//10+1):
        for y in range(n//10+1):
            matrix[x*10][y*10] = random.randint(1,1000)

    return matrix

def fcc(x1,y1,h1,x2,y2,h2,interx,intery) -> float:
    pass

def terrain_inter(M:list[list[int]]):
    pass

if __name__ == "__main__":
    n = int(input("value of n: ")) + 1
    M = generateMatrix(n)
    # print(M)

    time_before = time.time()
    terrain_inter(M)
    time_after = time.time()

    time_elapsed = time_after - time_before

    print(f"Time elapsed: {time_elapsed} seconds")