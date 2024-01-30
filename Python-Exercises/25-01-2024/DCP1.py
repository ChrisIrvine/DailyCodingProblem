# Exercise:
# Given a list of numbers and a number k, return whether any two of numbers
# add from the list add up to k.
#
# Example: given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

k = 17
numbers = [10, 15, 3, 7]

for i in numbers:
    for j in numbers:
        if(i + j == k):
            print(i, ' and ', j, ' equals ', k)
            break
        else:
            continue
    break