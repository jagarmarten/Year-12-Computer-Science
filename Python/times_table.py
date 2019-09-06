#User has to input a number between 1 and 10
#eg. if user inputs 3, the result will be as follows: 3 -> 3*1=3, 3*2=6, 3*3=9

#ask a user to input a number
number = int(input("Input number between 1 and 10: "))

#check whether the number is smaller or equal to 10 or greater or equal to 1
#if it's 
if number >=10 or number <=1:
    print("Number needs to be BETWEEN 1 and 10!")
else:
    #if the input number fits, do a for loop
    for x in range(number):
        table = (x+1) * number #multiply x by the inputted number
        print(str(x + 1) + " * " + str(number) + " = " + str(table)) #print out a result
