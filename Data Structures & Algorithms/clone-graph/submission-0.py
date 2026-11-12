"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}

        def dfs(node):

            if node in visited:
                return visited[node]

            # Create clone
            clone = Node(node.val)

            # Store mapping
            visited[node] = clone

            # Clone neighbours
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        if not node:
            return None

        return dfs(node)
            