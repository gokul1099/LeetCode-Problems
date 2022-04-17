# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = curr = TreeNode()
        stack = []
        def helper(root,ans):
            if(not root):
                return 
            
            helper(root.left,ans)
            stack.append(root.val)
            helper(root.right,ans)
        helper(root,ans)
        for i in stack:
            ans.right = TreeNode(i)
            ans = ans.right
        return curr.right