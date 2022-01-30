class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        hardest_job_remaining = [0]*len(jobDifficulty)
        hardest_job=0
        n = len(jobDifficulty)
        if n<d:
            return -1
        for i in range(n - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
        @lru_cache(None)    
        def helper(index,day):
            if d==day:
                return hardest_job_remaining[index]
            best = float("inf")
            hardest = 0
            for i in range(index,n-(d-day)):
                hardest = max(hardest,jobDifficulty[i])
                best = min(best,hardest+helper(i+1,day+1))
            return best
        return helper(0,1)
                
            
        