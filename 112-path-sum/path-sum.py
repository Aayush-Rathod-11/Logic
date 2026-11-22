# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        # Stack stores (node, remaining_sum_needed_from_this_node)
        stack = [(root, targetSum - root.val)]

        while stack:
            node, rem = stack.pop()

            # Leaf check: valid root-to-leaf path exists if remaining sum hits 0
            if not node.left and not node.right and rem == 0:
                return True

            if node.right:
                stack.append((node.right, rem - node.right.val))
            if node.left:
                stack.append((node.left, rem - node.left.val))

        return False