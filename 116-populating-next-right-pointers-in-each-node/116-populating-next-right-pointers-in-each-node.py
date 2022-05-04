"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def recur(left,right):
            if not left:
                return
            left.next = right
            recur(left.left,left.right)
            recur(left.right,right.left)
            recur(right.left,right.right)
        if(not root):
            return root
        recur(root.left,root.right)
        return root
        
            
        