/**
 * @param {string[]} ops
 * @return {number}
 */
var calPoints = function(ops) {
    let ans = []
    for(let index=0;index<ops.length;index++){
        let ansIndex = ans.length
        if(ops[index]==="C"){
            ans.pop()
        }
        else if(ops[index] === "+"){
            ans.push(parseInt(ans[ansIndex-1]) + parseInt(ans[ansIndex-2]))
        }
        else if(ops[index] === "D"){
            ans.push(ans[ansIndex-1] * 2)
        }
        else{
            ans.push(ops[index])
        }
    }
    return ans.reduce(function(a,b){return parseInt(a)+parseInt(b)},0)
    
};