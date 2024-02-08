# cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
# returns the first and last element of that pair. For example, 
# car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.


def car(f):
    # Define a data structure that is the reverse of the original pair 
    # (in order to access the individual components), as the original
    # pair is not iterable or subscriptable
    def pair(a, b):
        return a
    return f(pair)

def cdr(f):
    def pair(a, b):
        return b
    return f(pair)

print(car(cons(3,4)))
print(cdr(cons(3,4)))
