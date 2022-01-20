import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lIndex=1
        rIndex=max(piles)
        while(lIndex < rIndex ):
            mid = (lIndex + rIndex)//2
            tempRate=0
            for i in range(len(piles)):
                tempRate += math.ceil(piles[i] / mid)
            if(tempRate >h):
                lIndex = mid+1
            else:
                rIndex = mid
        return rIndex        
                
                
        