/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    let res =[]
    let row = grid.length
    let col = grid[0].length
    let totalLen = row * col
    k = k%totalLen
    for(let index1 =0;index1<row;index1++){
        let tempArr = []
        for(let index2 =0;index2<col;index2++){
            let flatIndex = (index1 * col+index2+totalLen-k)%totalLen
            tempArr.push(grid[parseInt(flatIndex/col)][parseInt(flatIndex%col)])
        }
        res.push(tempArr)
    }
    return res
};