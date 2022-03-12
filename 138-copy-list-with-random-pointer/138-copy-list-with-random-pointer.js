/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    let hash = new Map()
    let curr = head
    while(curr !=null){
        let copy = new Node(curr.val)
        hash.set(curr,copy)
        curr = curr.next
    }
    curr= head
    while(curr!=null){
        copy = hash.get(curr) || null
        copy.next = hash.get(curr.next) || null
        copy.random = hash.get(curr.random) || null
        curr = curr.next
    }
    return hash.get(head)
};