# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans=[]
        def helper(root,val):
            if root==None:
                return
            val.append(root.val)
            helper(root.right,val)
            helper(root.left,val)
            
        helper(root1,ans)
        helper(root2,ans)
        return sorted(ans)
        