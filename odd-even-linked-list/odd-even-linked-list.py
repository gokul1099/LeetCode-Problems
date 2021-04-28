# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        oddNode = head
        evenNode = head.next
        evenHead = head.next
        while(oddNode and evenNode and evenNode.next):
            odd = evenNode.next
            oddNode.next = odd
            evenNode.next = odd.next
            
            oddNode = oddNode.next
            evenNode = evenNode.next
        oddNode.next = evenHead
        return head
            
        
            
        
        