/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
var helper = function(root1,root2){
    if(!root1){
        return
    }
    if(!root2){
        return
    }
    if(root1 && root2){
        root1.val = root1.val+root2.val
    }
    if(root1.left && root2.left){
        helper(root1.left,root2.left)
    }
    else if(!root1.left && root2.left){
        root1.left = root2.left
    }
    if(root1.right && root2.right){
        helper(root1.right,root2.right) 
    }
    else if(!root1.right && root2.right){
        root1.right = root2.right
    }
    return
    
}
var mergeTrees = function(root1, root2) {
    if(!root1 && root2){
        return root2
    }
    if(root1 && !root2){
        return root1
    }
    helper(root1,root2)
    return root1
};