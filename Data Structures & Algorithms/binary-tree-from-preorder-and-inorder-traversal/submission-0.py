class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index = {value: i for i, value in enumerate(inorder)}  # Store each value's index in inorder
        preorder_index = 0  # Track the next value to use from preorder

        def dfs(left, right):  # Build a subtree within the given inorder boundaries
            nonlocal preorder_index  # Allow dfs to update preorder_index

            if left > right:  # If the range is empty, there is no node
                return None  # Return an empty child

            root_val = preorder[preorder_index]  # Get the next root from preorder
            preorder_index += 1  # Move to the next preorder value

            root = TreeNode(root_val)  # Create a node with the root value
            mid = inorder_index[root_val]  # Find the root's position in inorder

            root.left = dfs(left, mid - 1)  # Recursively build the left subtree
            root.right = dfs(mid + 1, right)  # Recursively build the right subtree

            return root  # Return the completed subtree

        return dfs(0, len(inorder) - 1)  # Build and return the entire tree