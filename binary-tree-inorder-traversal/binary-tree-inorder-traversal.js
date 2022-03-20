/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let ans = []
    let stack =[]
    let curr = root
    while(stack.length >0 || curr!=null){
        if(curr){
            stack.push(curr)
            curr=curr.left
        }
        else{
            curr = stack.pop()
            ans.push(curr.val)
            curr=curr.right
        }
    }
    return ans
    
};