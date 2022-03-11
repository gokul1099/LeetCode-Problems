/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if(head == null || head.next == null){
        return head
    }
    prev = head
    curr = head.next
    prev.next = null
    while(curr){
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    }
    return prev
};