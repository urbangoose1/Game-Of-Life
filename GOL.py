import random
import time
import os

#Conway's Game of Life
#alive=█, dead=" "
#Each cell in the grid is either alive (1) or dead (0).
#Rules:
#   Any live cell with two or three live cells survives.
#   Any dead cell with exactly three live cells becomes a live cell.
#   All other live cells die in the next generation. (if too much they also die)

def createGrid():
    rows = 45
    columns = 45
    grid = [[0 for _ in range(columns)] for _ in range(rows)] #Create empty grid with 0 for all list values
    for counter in range(rows): #Repeats for all rows and values in list
        for counter1 in range(columns):
            cell = random.randint(0,2) #Make a 33% for cell spawn on each space
            if cell == 0:
                grid[counter][counter1] = 1
            else:
                grid[counter][counter1] = 0
    
    return grid,rows,columns
            

def countCells(TL,T,TR,L,M,R,BL,B,BR): #TL stands for 'Top Left' and BR stands for 'Bottom Right' and so on
    neighbors = [TL,T,TR,L,R,BL,B,BR] #Group the values
    neighbors = [n for n in neighbors if n is not None] #Remove nil values
    total = sum(neighbors) #Add the live neighbours up

    if M == 1:
        return 1 if total in (2, 3) else 0 #Enforces the rules for live cells
    else:
        return 1 if total == 3 else 0 #Enforces the rules for dead cells


def generation(grid):
    height = len(grid)
    width = len(grid[0])

    newGrid = [[0 for _ in range(width)] for _ in range(height)] #Creates the new grid

    for y in range(height):
        for x in range(width):

            neighbours = []
            for cy in (-1,0,1): #Go through the three y layer neighbours
                for cx in (-1,0,1): #Go through the three x layer neighbours
                    if cy == 0 and cx == 0: #Exclude the cell which is the subject
                        continue
                    ny = y+cy #Specifies the y layer that the loop is on for the subject cell
                    nx = x+cx #Specifies the x point that the loop is on for the subject cell

                    if 0 <= ny and ny < height and 0 <= nx and nx <  width: #Makes sure the position is valid and not off grid
                        neighbours.append(grid[ny][nx])
                    else:
                        neighbours.append(None)
                    
            newGrid[y][x] = countCells(*neighbours[:3],neighbours[3],grid[y][x],neighbours[4],*neighbours[5:]) #Send the relevant positions through the module(* splits the list up into values)
    
    return newGrid

def displayGrid(grid,columns,rows):
    displayGrid = [[0 for _ in range(columns)] for _ in range(rows)] #Create a new grid to prevent overwritting original grid
    for y in range(len(grid)): #Go through all values
        for x in range(len(grid)):
            if grid[y][x] == 1:
                displayGrid[y][x] = "█" #Changes the 1 values to blocks to better represent it
            elif grid[y][x] == 0:
                displayGrid[y][x] = " " #Changes the 0 values to spaces to better represent it
    
    for counter in range(len(displayGrid)):
        print("".join(str(v) for v in displayGrid[counter])) #join the cells with empty characters




#Call modules
grid,columns,rows = createGrid() #Creates the origianl random grid
ticks = 0
while True:
    displayGrid(grid,columns,rows) #Displays the grid before changing it
    print("Ticks:",ticks)
    ticks += 1
    grid = generation(grid)
    time.sleep(0.4) #Refresh every 0.3 seconds
    os.system("cls") #What should replace this if deprecated?
