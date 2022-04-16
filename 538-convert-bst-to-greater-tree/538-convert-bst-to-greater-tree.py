# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if(root is not None):
        #     self.convertBST(root.right)
        #     self.total += root.val
        #     root.val = self.total
        #     self.convertBST(root.left)
        # return root    
        stack = []
        node = root
        while(node or stack):
            while(node is not None):
                stack.append(node)
                node = node.right
            node = stack.pop()
            self.total += node.val
            node.val = self.total
            node = node.left
        return root    
        