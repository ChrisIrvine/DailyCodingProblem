# Exercise:
#
# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the original
# array except the one at i. 
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output 
# would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected
# output would be [2, 3, 6].

# Brute forced

inputArray = [1, 2, 3, 4, 5]
inputLength = len(inputArray)
outputArray = [0] * inputLength

for i in range(inputLength):
    product = 1
    for j in range(inputLength):
        if i == j:
            continue
        product = product*inputArray[j]
    outputArray[i] = product

print("Output is: ", outputArray)

# Reset outputArray
outputArray = [0] * inputLength

# Refined attempt, removed if statement and nested for loop.

outputArray[0] = 1
for i in range(1, inputLength):
    outputArray[i] = inputArray[i-1] * outputArray[i-1]

suffixProduct = 1
for i in range(inputLength-1, -1, -1):
    outputArray[i] = outputArray[i] * suffixProduct
    suffixProduct = suffixProduct * inputArray[i]

print("The refined output is: ", outputArray)
