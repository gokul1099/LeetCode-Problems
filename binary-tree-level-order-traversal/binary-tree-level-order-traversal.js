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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if(!root){
        return []
    }
    let queue =[root]
    let ans = []
    while(queue.length){
        let lvl =[]
        let len = queue.length
        for(let i=0;i<len;i++){
            let temp = queue.shift()
            if(temp.left){
                queue.push(temp.left)
            }
            if(temp.right){
                queue.push(temp.right)
            }
            lvl.push(temp.val)
        }
        ans.push(lvl)
    }
    return ans
};