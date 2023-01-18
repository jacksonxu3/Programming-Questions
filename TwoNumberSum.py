# Two Number Sum
'''
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.
Note that the target sum has to be obtained by summing two different integers
in the array; you can't add a single integer to itself in order to obtain the
target sum.
You can assume that there will be at most one pair of numbers summing up to
the target sum.
'''
# O(n^2) Solution: 
def twoNumberSum(array, targetSum):
    for x in range(0, len(array)):
        for y in range(x+1, len(array)):
            if (array[x] + array[y] == targetSum):
                return [array[x], array[y]]
    return []

# O(n) Solution:
def twoNumberSumOptimal(array, targetSum):
        intSet = set(x for x in array)
    for y in array:
        targetInt = targetSum - y
        if (targetInt in intSet):
            if (targetInt != y):
                return [y, targetInt]
    return []
