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
#print(binary_search(my_list, 3)) # returns 1(this is the index position of the value we're looking for in the list)
#print(binary_search(my_list, -1)) # this value is not found in the list so it returns none

#print(binary_search(my_list, 5)) # value is found in list at index position 2 so that's what it will return

"""

Exercise 1 - If you have a sorted list of 128 names and you're searching through it using binary search, what's the maximum number of steps it would take 

Answer is 7

log128 = log(2)128 == 2^7 or 2 * 2 * 2 * 2 * 2 * 2 * 2 = 128

Solution is 7 

"""

# in a list of 128 values, find index position of 5, else return null

print(binary_search(range(128), 5)) #

# in a list of 128, values find value 128 (doesnt exist because lists in python are zero indexed, meaning highest posssible index is actually 127)
print(binary_search(range(128), 128)) # answer is None


"""
if you double the size of the list, what's the maximum number of steps now?

log256 == log(2)256 == 2^8 == 256

It would take 8 steps 

"""
