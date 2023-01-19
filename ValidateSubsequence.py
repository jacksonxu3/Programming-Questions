# Validate Subsequence

'''
Given two non-empty arrays of integers, write a function that determines whether the second array
is a subsequence of the first one.

A subsequence means that the order of the elements is the same as in the array.
'''

def isValidSubsequence(array, sequence):
    if (len(sequence) > len(array)):
        return False
    tracker = 0
    for x in range(0, len(sequence)):
        if (tracker >= len(array)):
            return False
        while(array[tracker] != sequence[x]):
            tracker += 1
            if (tracker >= len(array)):
                return False
        tracker += 1
    return True

# Cleaner version
def isValidSubsequence(array, sequence):
    if (len(sequence) > len(array)):
        return False
    tracker = 0
    # Run for loop over array rather than seq, because
    # len(seq) tells you the amount of required valid elements
    # and will perfectly match up with the tracker variable
    for x in array:
        if (tracker == len(sequence)):
            return True
        if (sequence[tracker] == x):
            tracker += 1
    return tracker == len(sequence)
