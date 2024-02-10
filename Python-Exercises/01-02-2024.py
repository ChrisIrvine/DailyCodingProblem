# A unival tree (which stands for "universal value") is a tree 
# where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Brute for method O(n^2) time
        
def is_unival(root):
    # Is root empty
    if root == None:
        return True
    
    # Check left value vs root value
    if root.left != None and root.left.value != root.value:
        return False
    
    # Check right value vs root value
    if root.right != None and root.right.value != root.value:
        return False
    
    # Check left vs right values
    if is_unival(root.left) and is_unival(root.right):
        return True
    
    return False

def count_univals(root):
    # Is tree empty
    if root == None:
        return 0

    # Get the left subtrees and right subtrees counts
    total_count = count_univals(root.left) + count_univals(root.right)

    # Check if the initial tree is unival
    if is_unival(root):
        total_count += 1

    return total_count

# More efficient method O(n) time
def count_univals2(root):
    total_count, is_unival = helper(root)
    return total_count

def helper(root):
    if root == None: return (0, True)

    # Get left and right counts
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)

    is_unival = True

    if not is_left_unival or not is_right_unival:
        is_unival = False
    if root.left != None and root.left.value != root.value:
        is_unival = False
    if root.right != None and root.right.value != root.value:
        is_unival = False
    
    if is_unival:
        return (left_count + right_count + 1, True)
    else: 
        return (left_count + right_count, False)

# Test tree
#         0
#        / \
#       1   0
#          / \
#         1   0
#        / \
#       1   1
# Expected output: 5 

root = Node(1)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1) 

print("Number of unival subtrees (brute force method): ", count_univals(root))
print("Number of unival subtrees (refined method): ", count_univals2(root))