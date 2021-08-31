# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr_1,ptr_2=head,head
        nth_ele =0
        while(nth_ele < n):
            ptr_2 = ptr_2.next
            nth_ele+=1
        if(not ptr_2):
            return head.next
        while(ptr_2.next):
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
        if(ptr_1.next):
            ptr_1.next = ptr_1.next.next
        else:
            ptr_1.next=None
            
        return head
        