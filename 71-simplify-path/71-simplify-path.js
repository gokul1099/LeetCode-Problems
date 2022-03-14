/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
     let arr = path.split(/\/\.\/|\/+/)
     let stack=[]
     arr.forEach(p=>{
    if(p){
        if(p==".."){
             stack.pop()
         }
        else if(p!=="."){
            stack.push(p)
        }
    }
})
return "/"+stack.join("/")
     
};