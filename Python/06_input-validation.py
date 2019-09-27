#User has to input a number between 1 and 10
#eg. if user inputs 3, the result will be as follows: 3 -> 3*1=3, 3*2=6, 3*3=9

#ask a user to input a number
number = int(input("Input number between 1 and 10: "))

#if the input number is 99 than exit the program
if number == 99:
    exit()
# end if

#if the number isn't the one we want, the user will have to submit it again
while number < 1 or number > 10:
    print("Number needs to be BETWEEN 1 and 10")
    number = int(input("Input number between 1 and 10: "))
# end while

#times table running in a for loop with a range of 12
for count in range(12):
    table = (count+1) * number #multiply count by the inputted number
    print(str(count + 1) + " * " + str(number) + " = " + str(table)) #print out a result
# end for

# 27.9.19 EDIT - updated variable naming