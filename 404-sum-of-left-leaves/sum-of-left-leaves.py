# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        total = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                left = node.left
                # Check if left child is a leaf directly from its parent
                if not left.left and not left.right:
                    total += left.val
                else:
                    stack.append(left)

            if node.right:
                stack.append(node.right)

        return total