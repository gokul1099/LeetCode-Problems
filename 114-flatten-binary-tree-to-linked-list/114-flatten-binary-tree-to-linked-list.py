# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.recur(root)
    def recur(self,root):
        if not root:
            return
        self.recur(root.right)
        self.recur(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
        

        
        