# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangeSum=[]
        def helper(root,low,high):
            if not root:
                return 
            helper(root.right,low,high)
            helper(root.left,low,high)
            if(root.val >=low and root.val<=high):
                   rangeSum.append(root.val)
            return
        helper(root,low,high)
        return sum(rangeSum)
        