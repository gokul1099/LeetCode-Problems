# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.curr = TreeNode(0)
        stack = []
        def helper(root):
            if(not root):
                return 
            helper(root.left)
            root.left= None
            self.curr.right = root
            self.curr = root
            helper(root.right)
        helper(root)
        return ans.right