/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function(head, k) {
    let dummy = new ListNode(0,head)
    let preLeft = dummy
    let preRight = dummy
    let left = head
    let right = head
    for(let index=0;index<k-1;index++){
        preLeft = left
        left= left.next
    }
    let temp = left
    while(temp.next){
        preRight = right
        right = right.next
        temp = temp.next
    }
    preRight.next = left
    preLeft.next = right
    temp = right.next
    right.next = left.next
    left.next = temp
    return dummy.next    
};