# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headCopy = head
        length = 0
        while(headCopy):
            length+=1
            headCopy = headCopy.next
        if(length%2==0):
            mid = (length//2)
        else:
            mid = length//2
        while(mid >0):
            head = head.next
            mid-=1
        
        return head   
        