#insertion sort function
def insertion_sort(list):
    list_length = len(list) #getting the size of the list
    for i in range(1, list_length):
        current_value = list[i] #getting the current value at list[i]
        position = i #getting the value from i and assigning it to position
        while position > 0 and list[position - 1] > current_value:
            list[position] = list[position - 1] #assign list[position] to list[position - 1]
            position = position - 1 #lower the position by one
        #ENDWHILE
        list[position] = current_value #set list[position] to the current value
    #ENDFOR
#END PROCEDURE

## Main program
#numbers = [9, 25, 7, 97, 3, 5, 54, 37, 55, 1000, 585, 0, -7, 50]  # numbers list
numbers = [3,5,8,17,12,15,18,23,1]  # numbers list
insertion_sort(numbers)
print("List's been sorted: " + str(numbers))