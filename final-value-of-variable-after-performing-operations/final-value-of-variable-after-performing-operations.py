class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
       
        for i in range(len(operations)):
            op = operations[i]
            if(op[0] == '-'):
                x-=1
            elif(op[0] == '+'):
                x+=1
            if(op[0] == 'X'):
                if(op[2]=="-"):
                    x-=1
                else:
                    x+=1
        return x             
                