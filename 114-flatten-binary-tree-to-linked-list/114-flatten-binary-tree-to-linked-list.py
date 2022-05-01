# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = []
        stack.append(root)
        while(stack):
            curr = stack.pop()
            if(not curr):
                continue
            if(curr.right):
                stack.append(curr.right)
            if(curr.left):
                stack.append(curr.left)
            if(stack):
                curr.right = stack[-1]
            curr.left = None    
    

        
        