#input three numbers, compare them and print out the larger one
number1 = int(input("First number: ")) #first number choice
number2 = int(input("Second number: ")) #second number choice
number3 = int(input("Third number: ")) #third number choice

#if the number1 is greater than number2, return number1
#otherwise return number2

if (number1 > number2 and number1 > number3):
    print(str(number1))
elif (number2 > number1 and number2 > number3):
    print(str(number2))
elif (number3 > number1 and number3 > number2):
    print(str(number3))
else:
    print(str(number1))

# end if

#TEST DATA
# Input 1, 17, 5 -> output 17
# Input 8, 7, 9 -> output 9
# Input -5,-5,4 -> output 4


## ACS - Very good indeed .. nice logic. Good variable names and good comments

# 27.9.19 EDIT - just added some test data