class Solution:
def numberOfArithmeticSlices(self, nums: List[int]) -> int:
def recur(index,ans):
if index<2:
return 0
res=0
if(nums[index] - nums[index-1] == nums[index-1] - nums[index-2]):
res=1+recur(index-1,ans)
ans+=res
else:
recur(index-1,ans)
return res
ans=0
recur(len(nums)-1,ans)
return ans