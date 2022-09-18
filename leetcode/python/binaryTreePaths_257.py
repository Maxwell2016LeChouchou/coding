# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        results = []
        s = str(root.val)
        def func(node, path):
            if node:
                if node.left or node.right:
                    if node.left:
                        func(node.left, path + "->{}".format(node.left.val))
                    if node.right:
                        func(node.right, path + "->{}".format(node.right.val))
                else:
                    results.append(path)
        func(root, s)
        return results


class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []

        def func(node, res, path):
            if node.left is None and node.right is None:
                res.append(path + str(node.val))
            if node.left:
                func(node.left, res, path+str(node.val)+'->')
            if node.right:
                func(node.right, res, path+str(node.val)+'->')
        res = []
        func(root, res, "")
        return res


class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        stack = [(root, "")]

        while stack:
            node, path = stack.pop()
            
            if node.left is None and node.rght is None:
                res.append(path + str(node.val))

            if node.left:
                stack.append((node.left, path + str(node.val) + '->'))
            if node.right:
                stack.append((node.right, path + str(node.val) +'->'))
        return res





