from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        queue = deque([root])
        result = []

        while len(queue) > 0:

            level = []
            level_size = len(queue)

            for i in range(level_size):

                node = queue.popleft()

                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level)

        return result