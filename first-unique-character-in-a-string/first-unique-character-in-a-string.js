/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let hashMap =new Map()
    for(ele of s){
        if(typeof hashMap.get(ele) === "undefined"){
          hashMap.set(ele,0)  
        }
        else{
            hashMap.set(ele,hashMap.get(ele)+1)
        }
    }
    for(let index=0;index<s.length;index++){
        if(hashMap.get(s[index]) == 0){
            return index
        }
    }
    return -1
};