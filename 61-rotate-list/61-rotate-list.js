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
var rotateRight = function(head, k) {
  let l =1
  let tempHead = head
  let ans
  if(head == null){
      return head
  }
  while(tempHead.next!=null){
      tempHead = tempHead.next
      l+=1
  }
    k=k%l
    tempHead.next = head
    tempNode = head
    let index = l-k-1
    while(index >0){
        tempNode = tempNode.next
        index-=1
    }
    ans = tempNode.next
    tempNode.next = null
    return ans
   
    
     
  
};