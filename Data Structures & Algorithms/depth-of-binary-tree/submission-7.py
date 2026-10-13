# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # again, we use recursion because it is DFS

        # base case - if no nodes
        if root == None:
            return 0
        else:
            depth = 1 # depth is at least 1 if there is a root
             # recursive case - we compute left depth and right depth individually and chose the max depth out of the 2
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            
            return max(left_depth, right_depth) + depth