/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var isIsomorphic = function(s, t) {
    if(s.length !== t.length){
        return false
    }
    let hash_s_t = new Map()
    let hash_t_s = new Map()
    for(let index=0;index<t.length;index++){
        let tVals =hash_s_t.get(s[index])
        let tValt = hash_t_s.get(t[index])
        if(typeof tVals === "undefined" && typeof tValt === "undefined"){
            hash_s_t.set(s[index],t[index])
            hash_t_s.set(t[index],s[index])
        }
        else if((hash_s_t.get(s[index]) !== t[index]) && (hash_t_s.get(t[index]) !== s[index])){
            return false
        }
    }
    return true
};