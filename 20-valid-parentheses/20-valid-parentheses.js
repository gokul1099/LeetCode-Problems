/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = []
    let hash = {"{":"}","[":"]","(":")"}
    let index=0
    while(index < s.length){
        if("[{(".includes(s[index])){
            stack.push(s[index])
        }
        else if(stack!=[] && hash[stack[stack.length -1]]==s[index]){
            stack.pop()
        }
        else{
            return false
        }
        index+=1
    }
    console.log(stack)
    return stack.length==0
};