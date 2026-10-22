# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float("-inf"), high=float("inf")) -> bool:
        #traverse tree using dfs
        #for each node at dfs, check isValidBST constraint

        if root is None:
            return True
        
        if root.val <= low or root.val >= high:
            return False

        left_valid = self.isValidBST(root.left, low, root.val)
        right_valid = self.isValidBST(root.right, root.val, high)

        return left_valid and right_valid