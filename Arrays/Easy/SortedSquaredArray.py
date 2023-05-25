# Sorted Squared Array

'''
Write a function that takes in a non-empty array of integers that are sorted in ascending order, and 
returns a new array of the same length with the squares of the original integers also sorted. 
'''

# Quick and Short Solution, O(n log n)
def sortedSquaredArray(array):
    unsortedSquares = [x*x for x in array]
    unsortedSquares.sort()
    return unsortedSquares

# Optimal Solution, O(n)
def sortedSquaredArray(array):
    # Split the array into positives and negatives
    negatives = []
    positives = []
    toReturn = []
    for number in array:
        if (number < 0):
            negatives.append(number**2)
        else:
            positives.append(number**2)
    # Keep track of what index you are at for the two new arrays
    nIndex = len(negatives) - 1
    pIndex = 0
    # Run a merge because both sides are already sorted
    while ((nIndex >= 0) and (pIndex < len(positives))):
        if (negatives[nIndex] < positives[pIndex]):
            toReturn.append(negatives[nIndex])
            nIndex -= 1
        else:
            toReturn.append(positives[pIndex])
            pIndex += 1
    # When one array is empty, add the rest of the other array 
    # into the array to be returned
    if (nIndex < 0):
        for x in range(pIndex, len(positives)):
            toReturn.append(positives[x])
    elif (pIndex >= len(positives)):
        for x in reversed(range(0, nIndex + 1)):
            toReturn.append(negatives[x])
    return toReturn
