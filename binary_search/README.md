# What is a Binary Search?
A binary search is an efficient way to find a value in a sorted list of elements in the fewest number of searches possible.

`Simple search` is where in a list of n values, you evaluate every single element in the list. This is inefficient and the longest possible route

In a binary search, you always start in the middle of the range and evaluate the median in a range of numbers, narrowing down your search until you've found the value; else return null

Ex Search for n in a list of 1024 elements 

log1024 = log2n 

Ask yourself: How many 2's do you need to multiply to get to 1024

2^10 = 1024

Solution: 10 

It would take max 10 guesses to find a value in a list of 1024

Binary search runs in `logarithmic time` which seeks to find a value by performing as few searches in a list as possible, always starting from the middle. As opposed to `linear time` which is longer, slower and evaluates every value in a list
