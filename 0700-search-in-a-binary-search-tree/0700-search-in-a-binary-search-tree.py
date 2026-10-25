# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, target: int) -> TreeNode | None:
        # base case
        if root == None:
            return None
        curr = root

        while curr != None:
            if curr.val == target:
                return curr
            elif curr.val < target:
                # right side
                curr = curr.right
            else:
                # left side
                curr = curr.left
        
        return None