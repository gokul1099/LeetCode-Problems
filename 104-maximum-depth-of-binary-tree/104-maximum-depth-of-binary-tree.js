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
 * @return {number}
 */
var height = function(root){
    if(!root){
        return 0
    }
    return Math.max(height(root.right),height(root.left))+1
}
var maxDepth = function(root) {
    return height(root)
};