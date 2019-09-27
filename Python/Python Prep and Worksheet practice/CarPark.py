carPark = [
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
]

#always ask the user for input
while True:
  row = int(input("Row location (1 to 10): ")) - 1 # -1 because arrays start from 0
  position = int(input("Position (1 to 6): ")) - 1

  #user input validation, if it's incorrect that user has to submit again
  if (row > -1) and (row < 11) and (position > -1) and (position < 7):
    #if there's a car parked already, user will have to submit again
    if carPark[row][position] == 1:
      print("You can't park there...")
    else:
      carPark[row][position] = 1
      print("You've parked in a row " + str(row + 1))
      print(carPark[row])
  else:
    print("Submit again...")