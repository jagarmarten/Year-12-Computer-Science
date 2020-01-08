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

path((0,0), (3,4))
