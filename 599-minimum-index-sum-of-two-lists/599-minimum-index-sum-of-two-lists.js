/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    let hash = new Map()
    let res=[]
    for(let index=0;index<list1.length;index++){
        hash.set(list1[index],index)
    }
    let minSum= Number.MAX_SAFE_INTEGER
    for(let index=0;index<list2.length;index++){
        let index2 = hash.get(list2[index])
        if(typeof index2!=="undefined"){
            let temp = index+index2
            if(temp < minSum){
                minSum = temp
                res =[]
                res.push(list2[index])
            }
            else if(temp == minSum){
                res.push(list2[index])
            }
            
        }
    }
    return res
    
};