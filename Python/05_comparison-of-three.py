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
