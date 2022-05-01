**method 1 using recursion : (reverse order) **
```
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
```
​
**method 2 using stack**
​