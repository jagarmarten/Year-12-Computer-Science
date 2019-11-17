#this is a slightly improved version of the bubble sort
#  this version won't do that unnecessary pass as bubble_sort-1.py does

numbers = [9, 25, 7, 97, 3, 5, 54, 37, 55, 1000, 585, 0, -7] #numbers list
list_length = len(numbers) #getting the length of the numbers list
flag = True #indicates when a swap is made
i = 0 #counter for the while loop

#while counter is smaller than list_length and flag is true,
while i < (list_length - 1) and flag == True:
    #set the flag to False at the beginning of each loop
    flag = False
    for j in range(list_length - i - 1):
        #condition which swaps numbers and also sets the flag to true
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
            flag = True
        #ENDIF
    #ENDFOR
    print(numbers)
    i = i + 1 #add one to i for proper function of the while loop
#ENDWHILE