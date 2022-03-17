# Takes list of max possible in a sorted list and item (the value we're trying to find)

# if item is in the list, return its position 

def binary_search(list, item):
    # these 2 variables keep track of which part of the list you'll search in and will update and change as you loop through the search
    # lowest possible value
    low = 0
    # highest value of search range 
    high = len(list) - 1

# loop through each search in the binary search
    while low <= high:
        # check middle element of list in binary search 
        mid = (low + high)
        # the new guess in every search
        guess = list[mid]
        # if the guess is the value return the position(value)
        if guess == item:
            return mid 
            # if guess is higher than the value we're looking for, update the highest value of our next search range in the overall list 
        if guess > item:
            high = mid - 1
            # if the value is lower than the value we're looking for, update the lowest value of our next search range in overall list
        else:
            low = mid + 1 
    return None 

# list of values we'll search through
my_list = [1, 3, 5, 7, 9]

# value we are looking for 
print(binary_search(my_list, 3)) # returns 1(this is the index position of the value we're looking for in the list)
print(binary_search(my_list, -1)) # this value is not found in the list so it returns none