#this bubble sort is doing one more pass through the list than it is necesarry
#bubble_sort-2.py is an improved version
numbers = [9,25,7,97,3,5,54, 35, 1] #list of numbers to sort
list_length = len(numbers) #get the length of the list 

#for loop with a range 0 to (list_length - 2)
for i in range(list_length - 2):
    #for loop with a range 0 to (list_length - 2 - i)
    for j in range(list_length - i - 1):
        #condition which checks if a number at position numbers[j] is greater than numbers[j+1]
        #if it is, create a new temporary variable temp and store the value of numbers into it
        #than, assign the smaller value to numbers[j] and the greater value to numbers[j+1]
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
        #ENDIF
    #ENDFOR
    print(numbers)
#ENDFOR
