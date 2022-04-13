/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    let ans= [...Array(n)].map(e=>Array(n).fill(0))
    let rowS =0;
    let rowE =n-1
    let colS =0
    let colE = n-1
    let val =0
    while(rowS <= rowE && colS <=colE){
        for(let index=colS;index<=colE;index++){
            val+=1
            ans[rowS][index] = val
        }
        for(let index=rowS+1;index<=rowE;index++){
            val+=1
            ans[index][colE] = val
        }
        if(rowS < rowE && colS < colE){
            for(let index=rowE-1;index > rowS;index--){
                val+=1
                ans[rowE][index] = val
            }
            for(let index=rowE;index>rowS;index--){
                val+=1
                ans[index][rowS] = val
            }
        }
        rowS++
        rowE--
        colS++
        colE--
    }
    return ans
        

};