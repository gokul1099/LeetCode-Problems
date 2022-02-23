# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resHead=res= ListNode()
        carry=0
        while(l1 or l2 or carry):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp = val1+val2+carry
            carry = 1 if temp>9 else 0
            temp = temp%10 if temp>9 else temp
            resHead.next = ListNode(temp)
            resHead=resHead.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next    
            
        