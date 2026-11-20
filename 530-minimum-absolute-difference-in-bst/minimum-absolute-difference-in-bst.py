# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        prev_val = None
        stack = []
        curr = root

        # Iterative inorder traversal visits BST values in sorted ascending order
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if prev_val is not None:
                diff = curr.val - prev_val
                if diff < min_diff:
                    min_diff = diff
                    if min_diff == 1:
                        return 1
            prev_val = curr.val
            curr = curr.right

        return int(min_diff)