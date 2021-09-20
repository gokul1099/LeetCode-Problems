# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        return self.mergeSort(head)
    def findMid(self,node):
        ptr1 = node
        ptr2 = node.next
        while( ptr2!=None and ptr2.next!=None):
            ptr1 = ptr1.next
            ptr2=ptr2.next.next
        return ptr1    
    def merge(self,node_1,node_2):
        resNode = ListNode()
        temp = resNode
        while(node_1!=None and node_2!=None):
            if(node_1.val < node_2.val):
                temp.next = node_1
                node_1 = node_1.next
            else:
                temp.next = node_2
                node_2 = node_2.next
            temp =temp.next
        if(node_1 !=None):
            temp.next = node_1
        if(node_2 !=None):
            temp.next = node_2
        return resNode.next
            
            
    def mergeSort(self,node):
        if node.next == None:
            return node
        mid = self.findMid(node)
        right = mid.next
        mid.next = None
        left = node
        leftNode =self.mergeSort(left)
        rightNode = self.mergeSort(right)
        return self.merge(leftNode,rightNode)
        
        
        