# Matrix of pages - 0 when there's no link, 1 when there is a link to another page
pages = [[0,1,1], 
        [1,0,0], 
        [1,0,0]]
# Outbound links from each page
outBoundLinks = [0,0,0]

#- Looping through the 2D array and figuring out the number of outbound links from each page
for x in range(len(pages)):
    for y in range(len(pages[x])):
        if pages[x][y] == 1:
            outBoundLinks[x] += 1

# Function used to prevent division by 0
def divisionByZeroCheck(n, d):
    return n / d if d else 0

# Initial page rank
pageRank = [1,1,1]
# Page Rank iteration
for iteration in range(3):
    value = 0
    # Ignore the iteration for page 1
    if iteration == 0:
        value += 0
    else:
        value += divisionByZeroCheck(pageRank[0],outBoundLinks[0])
    # Ignore the iteration for page 2
    if iteration == 1:
        value += 0
    else:
        value += divisionByZeroCheck(pageRank[1],outBoundLinks[1])
    # Ignore the iteration for page 3
    if iteration == 2:
        value += 0
    else:
        value += divisionByZeroCheck(pageRank[2],outBoundLinks[2])
    pageRank[iteration] = 0.15+0.85*(value)

print(pageRank) #print the values
# I spent hours trying to figure out why it doesn't work as it should - I think I might be missing something in my calculations...
