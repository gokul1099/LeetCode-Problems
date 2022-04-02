/**
 * @param {string} s
 * @return {boolean}
 */
var checkPalindrome = function(s,ind1,ind2){
    while(ind1 < ind2){
        if(s[ind1] !=s[ind2]){
            return false
        }
        ind1+=1
        ind2-=1
    }
    return true
}
var validPalindrome = function(s) {
    let index1= 0
    let index2 = s.length-1
    while(index1 < index2){
        if(s[index1] != s[index2]){
            return checkPalindrome(s,index1+1,index2) || checkPalindrome(s,index1,index2-1)
        }
        index1+=1
        index2-=1
    }
    return true
};