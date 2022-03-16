/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var transform=(str)=>{
    let res =""
    let hash = new Map()
    str.map((char,index)=>{
        if(typeof hash.get(char) ==="undefined"){
            hash.set(char,index.toString())
        }
        res+=hash.get(char)+" "
    })
    return res
}
var isIsomorphic = function(s, t) {
    return transform(s.split("")) === transform(t.split(""))
};