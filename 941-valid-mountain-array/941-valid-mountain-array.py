class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        count=0
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                count+=1
        if count == len(arr)-1 or count ==0:
            return False
        else:
            for i in range(count,len(arr)-1):
                if arr[i] > arr[i+1]:
                    count+=1
                else:
                    return False
        return True         
        