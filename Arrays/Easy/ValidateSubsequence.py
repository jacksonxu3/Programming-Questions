# Validate Subsequence

'''
Given two non-empty arrays of integers, write a function that determines whether the second array
is a subsequence of the first one.

A subsequence means that the order of the elements is the same as in the array.
'''
# Ugly version
def isValidSubsequence(array, sequence):
    # Subsequence array cannot be longer than original array
    if (len(sequence) > len(array)):
        return False
    tracker = 0
    # Loop over seq, and run while loop in the for loop. 
    # Stopping whenever a match is found
    for x in range(0, len(sequence)):
        # Make sure not out of bounds
        if (tracker >= len(array)):
            return False
        while(array[tracker] != sequence[x]):
            tracker += 1
            # Make sure not out of bounds
            if (tracker >= len(array)):
                return False
        # When a match is found, make sure that the current item in
        # array is not used again
        tracker += 1
    return True

# Cleaner version
def isValidSubsequence(array, sequence):
    # Subsequence array cannot be longer than original array
    if (len(sequence) > len(array)):
        return False
    tracker = 0
    # Run for loop over array rather than seq, because
    # len(seq) tells you the amount of required valid elements
    # and will perfectly match up with the tracker variable
    for x in array:
        # If we reach the end of the sequence, all is good
        if (tracker == len(sequence)):
            return True
        # Go onto the next item in seq if a match is found
        if (sequence[tracker] == x):
            tracker += 1
    # Always returns False, as reached the end of the original
    # array without going through the entire seq
    return tracker == len(sequence)
