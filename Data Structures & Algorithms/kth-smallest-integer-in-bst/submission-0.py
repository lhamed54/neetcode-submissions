# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #smallest is on the far left
        #largest is on the far right
        #so, start from far left, and go back k times

        arr = []

        def inOrder(node):

            if node is None:
                return 
            inOrder(node.left)
            arr.append(node.val)
            inOrder(node.right)

        inOrder(root)
        return arr[k-1]