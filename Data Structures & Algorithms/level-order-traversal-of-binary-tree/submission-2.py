
from collections import deque  # Import deque, which lets us efficiently remove items from the front of a queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # root is the starting node of the binary tree
        # We return a list of lists, with each inner list representing one level
        if root is None:  # Check if the tree is empty
            return []     # If there are no nodes, return an empty list
        queue = deque([root])  # Start the queue with the root node
        result = []             # Store the values of all levels here
        while len(queue) > 0:  # Continue while there are nodes left to process
            level = []              # Store the values for the current level
            level_size = len(queue) # Count how many nodes are at this level
            # Process only the nodes that were in the queue at the start of this level
            for i in range(level_size):
                node = queue.popleft()  # Remove the next node from the front of the queue
                level.append(node.val)  # Add this node's value to the current level
                if node.left is not None:  # Check whether this node has a left child
                    queue.append(node.left)  # Add the left child to the queue for the next level
                if node.right is not None:  # Check whether this node has a right child
                    queue.append(node.right)  # Add the right child to the queue for the next level
            result.append(level)  # We finished this level, so add it to the final result
        return result  # Return all levels as a nested list
