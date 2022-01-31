class Solution:
def climbStairs(self, n: int) -> int:
@lru_cache(None)
def solve(step):
if step==n:
return 1
if step>n:
return 0
return solve(step+1) + solve(step+2)
return solve(0)
​