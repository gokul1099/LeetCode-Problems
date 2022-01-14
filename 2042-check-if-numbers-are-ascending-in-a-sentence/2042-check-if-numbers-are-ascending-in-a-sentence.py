class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums =[]
        s=s.split(" ")
        for i in range(len(s)):
            if s[i].isdigit():
                nums.append(int(s[i]))
        count=0 
        print(nums)
        for i in range(len(nums)-1,0,-1):
            if(nums[i]> nums[i-1]):
                count+=1
        if(nums[0] < nums[1] and count == len(nums)-1):
            return True
        else:
            return False
             
                
            