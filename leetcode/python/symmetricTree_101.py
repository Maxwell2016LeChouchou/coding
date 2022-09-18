# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def sym(p,q):
        if p is None and q:
            return False
        if q is None and p:
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False
        return sym(p.left, q.right) and sym(p.right, q.left)
    return sym(root, root)