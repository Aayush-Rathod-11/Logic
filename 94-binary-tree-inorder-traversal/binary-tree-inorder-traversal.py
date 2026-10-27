# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Dive as far left as possible, pushing nodes onto the stack
            while current:
                stack.append(current)
                current = current.left
                
            # Pop the leftmost node
            current = stack.pop()
            result.append(current.val)
            
            # Move to its right subtree
            current = current.right
            
        return result