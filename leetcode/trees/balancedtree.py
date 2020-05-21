# Question — Balanced Binary Tree:
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# Analysis:
#
# It is a question about recursion. Need to realize: program needs to judge for each pair of left
# and right nodes that
# if their maximum/minimum depths are not different greater than 1
# (Judgement for only root.left and root.right is not enough, need to do for each pair of .left
# and .right).



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None: return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def maxDepth(self, root):
        if root == None: return 0
        if root.left == None and root.right == None: return 1
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)