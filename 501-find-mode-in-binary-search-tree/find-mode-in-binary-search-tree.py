# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        modes = []
        max_count = 0
        curr_count = 0
        curr_val = None
        
        def inorder(node):
            nonlocal max_count, curr_count, curr_val, modes
            if not node:
                return
            
            inorder(node.left)
            
            # Process current node value
            if node.val == curr_val:
                curr_count += 1
            else:
                curr_val = node.val
                curr_count = 1
                
            if curr_count > max_count:
                max_count = curr_count
                modes = [curr_val]
            elif curr_count == max_count:
                modes.append(curr_val)
                
            inorder(node.right)
            
        inorder(root)
        return modes