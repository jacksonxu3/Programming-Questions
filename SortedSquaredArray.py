# Sorted Squared Array

'''
Write a function that takes in a non-empty array of integers that are sorted in ascending order, and 
returns a new array of the same length with the squares of the original integers also sorted. 
'''

# Quick and Short Solution, O(nlog x)
def sortedSquaredArray(array):
    # List comprehension
    unsortedSquares = [x*x for x in array]
    unsortedSquares.sort()
    return unsortedSquares

# Optimal Solution
