/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    let arr = s.split("")
    let stack = []
    for(let index=0;index<arr.length;index++){
        if(arr[index] == "("){
            stack.push(index)
        }
        else if(arr[index]==")"){
            if(stack.length>=1){
                stack.pop()
            }
            else{
                arr[index]=""
            }
        }
    }
    if(stack.length>=1){
        stack.forEach(index=>{
            arr[index] = ""
        })
    }
    return arr.join("")
};