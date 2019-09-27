#run it on repl.it - https://repl.it/@MartinDevMan/Array-Game

game = [
  ['O','X','X','X'],
  ['X','X','X','X'],
  ['X','X','X','X'],
  ['X','X','X','X'],
  ['X','X','X','X'],
  ['X','X','X','X']
]

def matrixFrom2DArray (array):
  #found an answer on Quora - https://qr.ae/TWsovJ
  #printing the 2D array in a form of matrix
  for row in array:
    for element in row:
      print(element, end='\t')
    print('\n')

while True:
  row = int(input("Row (between 1 and 6): ")) - 1
  collumn = int(input("Collumn (between 1 and 4): ")) - 1

  #input vaidation - checks whether the input numbers are correct
  if (row > -1) and (row < 7) and (collumn > -1) and (collumn < 5):
    #the for below replaces the original "O" with "X"
    for i in range(0, 5):
      for j in range(0,4):
        if game[i][j] == "O":
          game[i][j] = "X"

    #creating a new "O" in the matrix
    game[row][collumn] = "O"

    #printing it out with my function
    matrixFrom2DArray(game)
  else:
    #if the numbers input weren't correct
    print("Submit again..." + '\n')