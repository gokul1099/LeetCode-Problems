class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursion(left,right,s):
            if left > right:
                return
            s[left],s[right] = s[right],s[left]
            recursion(left+1,right-1,s)
        recursion(0,len(s)-1,s)     