from math import sqrt #importing the sqrt function from math

#defining the grid we'll be working with
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

#start at pos 0,0; Find shortest way to pos 3,4
def path (start, end):
    start_x, start_y = start
    end_x, end_y = end
    grid[start_x][start_y] = 1 #number 1 represents the initial position
    grid[end_x][end_y] = 2 #number 2 represents the final destination
    
    found = False #will be set to True once the number is found
    path = 0 #this will be the distance in the grid

    air_distance = sqrt((start_x - end_x) ** 2 + (start_y - end_y) ** 2) #the distance "by air"
    print(distance)

path((0,0), (3,4))
