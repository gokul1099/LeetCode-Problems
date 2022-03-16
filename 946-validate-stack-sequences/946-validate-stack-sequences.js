/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
    let count =0;
    let stack = []
    for(let ele of pushed){
        stack.push(ele)

        while(stack.length>=1 && count < popped.length && stack[stack.length -1] == popped[count]){
            stack.pop()
            count+=1
        }

    }
    return count==popped.length
};