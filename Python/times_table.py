#User has to input a number between 1 and 10
#eg. if user inputs 3, the result will be as follows: 3 -> 3*1=3, 3*2=6, 3*3=9

number = int(input("Input number between 1 and 10: "))

if number >=10 or number <=1:
    print("Number needs to be BETWEEN 1 and 10!")
else:
    for x in range(number):
        table = (x+1) * number
        print(str(x + 1) + " + " + str(number) + " = " + str(table))
    
#if number >= 10 or number <= 1:
#    print("You've inputed a wrong number. It has to be higher than 1 and smaller than 10")
#else:
    
#endif
