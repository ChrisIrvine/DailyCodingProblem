# Given a list of integers, write a function that returns 
# the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Recursive approach
def recursive_max (inputArray, i):
    # check for array of one
    if i == 0:
        return inputArray[i]
    # check for array of two
    if i == 1:
        return max(inputArray[i-1], inputArray[i])
    else:
        return max(recursive_max(inputArray, i-1), inputArray[i] + recursive_max(inputArray, i-2))
    
# Dynamic approach
def dynamic_max (inputArray):
    # create a cache array based on length of input array
    cache = [0 for x in range(len(inputArray))]
    # assign first value
    cache[0] = inputArray[0]
    # assign the larger of the two variables
    cache[1] = max(inputArray[0], inputArray[1])
    # iterate finding the largest non-adjacent variables
    for i in range(2, len(inputArray)):
        cache[i] = max(cache[i-1], inputArray[i] + cache[i-2])
    return cache[-1]
    

# Constant Space approach
def constant_max (inputArray):
    incl, excl, = inputArray[0], 0
    # iterate over the array, adding the inclusive value to the temporary value or discarding it 
    # in favor of the larger exclusive value
    for i in range(1, len(inputArray)):
        tmp, excl = excl + inputArray[i], max(incl, excl)
        incl = tmp
    return max(incl, excl)

inputArray = [2, 4, 6, 2, 5]
i = len(inputArray) - 1
print(recursive_max(inputArray, i))
print(dynamic_max(inputArray))
print(constant_max(inputArray))