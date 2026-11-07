# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
            
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push left child first so that right child is processed first 
            # (yielding Root -> Right -> Left order)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        # Reverse the result to get Left -> Right -> Root (Postorder)
        return result[::-1]