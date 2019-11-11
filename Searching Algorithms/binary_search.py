# functions
def binary_search(sought_item, list):
    def midpoint(front, rear):
        return math.floor(float(start + end / 2))
    # END FUNCTION
    
    found = False
    index = -1
    start = 0
    end = len(list) - 1

    while start <= end and not found:
        midpoint = int((start + end / 2))
        if sought_item == list[midpoint]:
            found = True
            index = midpoint
        else:
            if sought_item < list[midpoint]:
                end = midpoint - 1
            else:
                start = midpoint + 1
        print(start, midpoint, end, index)
    return index
# END FUNCTION

## main code
import math
import random

from list_of_numbers import numbers  # importing the names list from list_of_names.py

searched_number = int(input("What name are you searching for?")) #ask user what name they want to search for
position = binary_search(searched_number, numbers)

if position == -1:
    print("Number " + str(searched_number) + " wasn't found in the list.")
else:
    print("Number " + str(searched_number) + " was found at position " + str(position) + " in the numbers list")
# ENDIF
