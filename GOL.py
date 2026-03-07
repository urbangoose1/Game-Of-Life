import random
import time
import os

#cell=█, dead=" "
#Conway's Game of Life
#Each cell in the grid is either alive (1) or dead (0).
#Rules:
#   Any live cell with two or three live cells survives.
#   Any dead cell with exactly three live cells becomes a live cell.
#   All other live cells die in the next generation. (if too much they also die)

def createGrid():
    rows = 50
    columns = 50
    grid = [[0 for _ in range(columns)] for _ in range(rows)]
    for counter in range(rows):
        for counter1 in range(columns):
            cell = random.randint(0,2)
            if cell == 0:
                grid[counter][counter1] = 1
            else:
                grid[counter][counter1] = 0
    
    return grid,rows,columns
            

def countCells(TL,T,TR,L,M,R,BL,B,BR):
    neighbors = [TL,T,TR,L,R,BL,B,BR]
    neighbors = [n for n in neighbors if n is not None]
    total = sum(neighbors)

    if M == 1:
        return 1 if total in (2, 3) else 0
    else:
        return 1 if total == 3 else 0


def generation(grid):
    height = len(grid)
    width = len(grid[0])

    newGrid = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):

            neighbours = []
            for cy in (-1,0,1):
                for cx in (-1,0,1):
                    if cy == 0 and cx == 0:
                        continue
                    ny = y+cy
                    nx = x+cx

                    if 0 <= ny and ny < height and 0 <= nx and nx <  width:
                        neighbours.append(grid[ny][nx])
                    else:
                        neighbours.append(None)
                    
            newGrid[y][x] = countCells(*neighbours[:3],neighbours[3],grid[y][x],neighbours[4],*neighbours[5:]) #btw * just splits the list up into values
    
    return newGrid

def displayGrid(grid,columns,rows):
    displayGrid = [[0 for _ in range(columns)] for _ in range(rows)]
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 1:
                displayGrid[y][x] = "█"
            elif grid[y][x] == 0:
                displayGrid[y][x] = " "
    #join the cells
    
    for counter in range(len(displayGrid)):
        print("".join(str(v) for v in displayGrid[counter]))




#Call modules
grid,columns,rows = createGrid()
while True:
    displayGrid(grid,columns,rows)
    grid = generation(grid)
    time.sleep(0.3)
    os.system("cls")