# Given an array of integers, find the first missing positive integer 
# in linear time and constant space. In other words, find the lowest 
# positive integer that does not exist in the array. The array can 
# contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. 
# The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

input = [3, 4, -1, 1, 1]
inputLength = len(input)

# Remove duplicates and order positive integers

input = list(set(input))

# Remove negative integers

input = list(filter(lambda x : x > 0, input))

# Remove numbers larger than the length of the list (as they will not be the lowest missing number)

input = list(filter(lambda x : x < len(input)+1, input))

# Determine the missing number

missing = 0
for i in range(1, inputLength):
    if i not in input:
        missing = i
        break
    else:
        missing = inputLength

print("The lowest missing positive integer is ", missing)

