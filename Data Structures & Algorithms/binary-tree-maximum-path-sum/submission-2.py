class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")  # Initialise the maximum sum to negative infinity to handle all-negative trees.

        def dfs(node):  # Define a recursive DFS function to explore each node.
            nonlocal max_sum  # Allow dfs to update max_sum from the outer function.

            if node is None:  # Base case: if the node doesn't exist, stop recursion.
                return 0  # An empty subtree contributes zero to the path sum.

            left = max(dfs(node.left), 0)  # Get the best left path sum, ignoring it if negative.
            right = max(dfs(node.right), 0)  # Get the best right path sum, ignoring it if negative.

            path_sum = node.val + left + right  # Calculate the path sum through this node using both branches.
            max_sum = max(max_sum, path_sum)  # Update the maximum sum if this path is better.

            return node.val + max(left, right)  # Return only the better branch so the parent can extend the path.

        dfs(root)  # Start DFS from the root to process every node.
        return max_sum  # Return the maximum path sum found anywhere in the tree.