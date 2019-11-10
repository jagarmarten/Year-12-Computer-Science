#functions
def linear_search(sought_item, array):
    found = False #setting the initial val of found to False
    index = -1 #setting index to -1 - it's useful to determine whether an item was or wasn't found
    count = 0 #setting the counter variable used in the while loop

    #continue iterating, while count is smaller than the length of array and the item wasn't found
    while count < len(array) and not found:
        #if the name at position count is the exact same as the one we're searching for, do these steps:
        if names[count] == sought_item:
            index = count #giving the value of count to index
            found = True #setting found to True stops the while loop from further iteration
            return index #returning the index
        # ENDIF
        count = count + 1 #if the name wasn't found, do another interation
        print(count) #print the count for informational purpouses
    # ENDWHILE
    return index #return the default val of index if the item wasn't found in the list
# ENDFUNCTION

## main code
from list_of_names import names  # importing the names list from list_of_names.py
searched_name = input("What name are you searching for?") #ask user what name they want to search for

index = linear_search(searched_name, names) #calling the function

#if the value returned in function is -1, it means that the item wasn't found
#if the val, is however greater than -1, it means that we've found the item
if index == -1:
    print("Name " + searched_name + " wasn't found in the list.")
else:
    print("Name " + searched_name + " was found at position " + str(index))
# ENDIF