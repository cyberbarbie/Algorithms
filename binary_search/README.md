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

## Calculating runtime
`Runtime` - How long it takes for an operation to complete

Let's say you're writing an algorithm that evaluates a list of 1 billion values in a list and 1 element equates to 1 millisecond:

In a Simple search algorithm, it would take 1 billion ms to complete (11 days)

In a Binary search algorithm, it would take only 30 ms to complete 
O(log1000000000) = 2 ^ 30 

It's not enough to know how long an algorithm takes to run, you need to know how the running time increases as the list size increases 

## Big O Notation 
Tells you how many operations it will take for an algorithm to complete 

Simple search algorithms run in O(n) runtime and binary search run in O(log n) runtime 

So, for example, calculate the O(n) and O(log n) runtimes (number of operations) it will take to draw a grid of 16 squares in simple vs binary search

### Simple Search
O(n) = O(16)
It will take 16 operations to complete

### Binary Search
O(log n) = O(log 16) = 2^4 = 16 
It will take 4 operations to complete 

Big O is about worse-case scenario -- like at worst it'll take 16 operations to find what you're looking for  

## Common Big O Run Times Sorted From Fastest to Slowest
`O (log n)` Logarithmic Time Ex. Binary search
`O(n)` Linear Time Ex. Simple Search
`O(n * log n)` Ex. Fast sorting algorithm Ex. quicksort
`O(n^2)` Ex. Slow Sorting Algorithm like selection sort
`O(n!)` Ex. A really slow algorithm like the traveling salesperson

### Summary
Algorithm speed isn't measured in seconds but in growth of the number of operations

Runtime of algorithms is expressed in Big O notation

O(log n) is faster than O(n) but it gets faster as the list of items you're searching grows 


