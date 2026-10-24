# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__ (self):
        self.ans = []

    def preorder(self, root):
        # Base case
        if root is None:
            return
        # Recursive case
        self.ans.append(root.val)
        self.preorder(root.left) # Left subtree
        self.preorder(root.right) # Right subtree

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:

        self.ans  = []
        # Start recursion from the root
        self.preorder(root) 
        return self.ans
        