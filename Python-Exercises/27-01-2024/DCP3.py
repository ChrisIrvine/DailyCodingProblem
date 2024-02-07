# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.
# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The following test should pass
# assert deserialize(serialize(node)).left.left.val == 'left.left'

node = Node('root', Node('left', Node('left.left')), Node('right'))
s = ""
i = 0   

def serialize(node, s=""):
    if(not node):
        s += "# "
        return s
    s += (str(node.val) + " ")
    s = serialize(node.left, s=s)
    s = serialize(node.right, s=s)
    return s

def deserialize(s):
    global i

    if s[i] == "#":
        if(i < len(s)-2):
            i += 2
        return None
    else:
        space = s[i:].find(" ")
        sp = space + i
        node = Node(s[i:sp])
        i = sp + 1 
        node.left = deserialize(s)
        node.right = deserialize(s)
        return node

print("Serialized string: " + serialize(node))
print("Assert: ", deserialize(serialize(node)).left.left.val == 'left.left')