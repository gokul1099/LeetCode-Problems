/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var reverse=function(nums,index1,index2){
    while(index1 < index2){
        let temp = nums[index1]
        swap(nums,index1,index2)
        index1+=1
        index2-=1
    }
}
var swap = function (nums,index1,index2){
    let temp = nums[index1]
    nums[index1] = nums[index2]
    nums[index2] = temp 
}

var nextPermutation = function(nums) {
    let index =nums.length -2
    while(index>=0 && nums[index+1] <= nums[index]){
        index-=1
    }
    if(index>=0){
        let j = nums.length - 1
        while(nums[j] <= nums[index]){
            j-=1
        }
        swap(nums,index,j)
    }
    reverse(nums,index+1,nums.length-1)
    
    
};