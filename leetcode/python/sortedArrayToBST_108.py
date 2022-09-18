# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sortedArrayToBST(nums):
    def balanceTree(left, right):
        if left > right:
            return None
        mid = (left+right)//2
        newNode = TreeNode(nums[mid])
        newNode.left = balanceTree(left, mid-1)
        newNode.right = balanceTree(mid+1, right)
        return newNode
    
    return balanceTree(0, len(nums)-1)
  

