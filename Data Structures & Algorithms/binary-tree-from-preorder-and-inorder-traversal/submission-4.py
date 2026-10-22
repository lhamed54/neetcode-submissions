# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # store where each value appears in inorder
        index_map = {}

        for i in range(len(inorder)):
            index_map[inorder[i]] = i

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            # no nodes left in this section
            if left > right:
                return None

            # first unused preorder value is the root
            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            # find root position in inorder
            root_index = index_map[root_val]

            # build left subtree
            root.left = build(left, root_index - 1)

            # build right subtree
            root.right = build(root_index + 1, right)

            return root

        return build(0, len(inorder) - 1)