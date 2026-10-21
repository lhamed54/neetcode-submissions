# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #access tree p using dfs
        #access tree q using dfs
        #return tree p == tree q

        if p is None and q is None:
            return True
        
        if p is None and q:
            return False
        
        if p and q is None:
            return False
        
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left == True and right == True
        