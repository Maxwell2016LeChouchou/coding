# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def isSameTree(p, q):
    def preOrder(node, tree):
        if node:
            tree.append(node.val)
            preOrder(node.left, tree)
            preOrder(node.right, tree)
        else: 
            tree.append(-1)
        return tree
    
    return (preOrder(p,[]) == preOrder(q, []))
