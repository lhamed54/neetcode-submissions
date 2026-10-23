# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #adjacent = current and left and right nodes
        #go through each node using dfs, see if it has left and right node
        #sum of adjacents = root.val + root.left.val + root.right.val
        #make sum of adjacents, add them to a list, then find maximum sum

        '''

        max_sum = 0

        if root is None:
            return 0
        
        if root.left is None:
            return
        
        if root.right is None:
            return

        pathsum = root.val + root.left.val + root.right.val
        max_sum = max(max_sum, pathsum)

        self.maxPathSum(root.left)
        self.maxPathSum(root.right)

        return max_sum

        '''


        '''
        def dfs(root):
            if root is None:
                return
            
            print(root)
            dfs(root.left)
            dfs(root.right)

        while root:
            if root.left and root.right:
                curr_sum = root.val + root.left.val + root.right.val
        '''

        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum

            if node is None:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            path_sum = node.val + left + right
            max_sum = max(max_sum, path_sum)

            return node.val + max(left, right)

        dfs(root)
        return max_sum


