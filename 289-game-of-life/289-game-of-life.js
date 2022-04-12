/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var checkBoundary = function(row,col){
    if(row <0 || row >=n || col <0 || col >=m ){
        return false
    }
    return true
}
var n;
var m;
var gameOfLife = function(board) {
    let res=[]
    n = board.length
    m = board[0].length
    for(let row=0;row<n;row++){
        let temp = []
        let sum=0
        for(let col =0;col<m;col++){
            sum=0
            sum +=checkBoundary(row,col-1) ? board[row][col-1]:0                       
            sum +=checkBoundary(row,col+1) ? board[row][col+1]:0
            sum +=checkBoundary(row-1,col-1) ? board[row-1][col-1]:0                   
            sum +=checkBoundary(row-1,col) ? board[row-1][col]:0                       
            sum +=checkBoundary(row-1,col+1) ? board[row-1][col+1]:0                   
            sum +=checkBoundary(row+1,col-1) ? board[row+1][col-1]:0                   
            sum +=checkBoundary(row+1,col) ? board[row+1][col]:0                       
            sum +=checkBoundary(row+1,col+1) ? board[row+1][col+1]:0                   
            if(board[row][col]==1){
                if(sum<2 || sum >3){
                    temp.push(0)
                }
                else{
                    temp.push(1)
                }
            }
            else{
                temp.push(sum===3?1:0)
            }
        }
        res.push(temp)
    }
    for(let row=0;row<n;row++){
        for(let col=0;col<m;col++){
            board[row][col] = res[row][col]
        }
    }
};