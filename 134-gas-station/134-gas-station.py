class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalCost = 0
        currCost = 0
        start = 0
        for i in range(len(gas)):
            remaining = gas[i] - cost[i]
            if(currCost < 0):
                start =i
                currCost = remaining
            else:
                currCost += remaining
            totalCost += remaining
        if(totalCost <0):
            return -1
        else:
            return start
                
            
        