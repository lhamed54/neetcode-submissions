# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:

    def serialize(self, root):
        values = []  # Create a list to store node values in preorder.

        def dfs(node):  # Traverse the tree using DFS (node, left, right).
            if node is None:  # Check if the current node is missing.
                values.append("N")  # Store "N" to represent a missing child.
                return  # Stop exploring this branch.

            values.append(str(node.val))  # Store the current node's value as a string.
            dfs(node.left)  # Recursively serialize the left subtree.
            dfs(node.right)  # Recursively serialize the right subtree.

        dfs(root)  # Start DFS from the root node.
        return ",".join(values)  # Combine values into one comma-separated string.

    def deserialize(self, data):
        values = data.split(",")  # Split the serialized string into a list of values.
        i = 0  # Initialise a pointer to track the next value to read.

        def dfs():  # Recursively reconstruct the tree from the values.
            nonlocal i  # Allow dfs to update the pointer i from the outer function.

            if values[i] == "N":  # Check whether the next value represents a missing node.
                i += 1  # Move the pointer to the next value.
                return None  # Return None to represent the missing child.

            node = TreeNode(int(values[i]))  # Create a node using the current value.
            i += 1  # Advance the pointer after consuming this node's value.

            node.left = dfs()  # Reconstruct the left subtree recursively.
            node.right = dfs()  # Reconstruct the right subtree recursively.

            return node  # Return the node with its left and right subtrees attached.

        return dfs()  # Start rebuilding the tree and return the root.

