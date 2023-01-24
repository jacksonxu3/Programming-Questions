# Nonconstructible Change

'''
Given an array of positive integers, determine the smallest integer 
that cannot be created by summing any amount of the given integers. 
'''


# Optimal solution, O(n log n)
def nonConstructibleChangeOptimal(coins):
  # Return 1 if the array is empty
    if len(coins) == 0:
        return 1
    # Sort the coins
    coins.sort()
    # Keep track of the maximum value that you have created
    # Allow the algorithm to end early in certain cases
    sum = 0
    # Run a for loop over all of the sorted coins
    for coin in coins:
        # Return if there is at least a 1 integer gap between the 
        # previous coins' sum max and the next coin
        if coin > sum + 1:
            return sum + 1
        # Otherwise, add onto the sum and go onto the next integer
        else:
            sum += coin
    # If we reach the last coin, then just return total sum + 1
    return sum + 1
