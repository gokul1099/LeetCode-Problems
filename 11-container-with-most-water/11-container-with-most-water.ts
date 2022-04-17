function maxArea(height: number[]): number {
    let index1: number = 0
    let index2: number = height.length
    let maxAmt: number = 0
    let val: number = 0
    while(index1 < index2){
        if(height[index1] < height[index2]){
            val = (index2 -index1) * height[index1]
            index1+=1
        }
        else{
            val = (index2 - index1) * height[index2]
            index2-=1
        }
        if(maxAmt < val){
            maxAmt = val
        }
        
    }
    
    return maxAmt
};