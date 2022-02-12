# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        while(list1):
            heapq.heappush(heap,list1.val)
            list1 = list1.next
        while(list2):
            heapq.heappush(heap,list2.val)
            list2 = list2.next
        ans =ansHead=ListNode()
        while(heap!=[]):
            ans.next = ListNode(heapq.heappop(heap))
            ans = ans.next
        return ansHead.next