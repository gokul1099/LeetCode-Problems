# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        val1=[]
        val2=[]
        def helper(root,val):
            if root==None:
                return
            val.append(root.val)
            helper(root.right,val)
            helper(root.left,val)
            return val
            
        val1 = helper(root1,val1)
        val2 = helper(root2,val2)
        if val1 and val2:
            return sorted(val1+val2)
        elif(val1 and not val2):
            return sorted(val1)
        elif(val2 and not val1):
            return sorted(val2)
        