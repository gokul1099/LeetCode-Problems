# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = {}
        if(head == None):
            return head
        if(head.next == None):
            return head
        temp = head.next
        prev = head
        while(temp.next!= None):
            if(temp.val == prev.val):
                prev.next= temp.next
                temp = temp.next
            else:    
                prev=prev.next
                
        if(temp.val == prev.val):
            prev.next= None
        return head    