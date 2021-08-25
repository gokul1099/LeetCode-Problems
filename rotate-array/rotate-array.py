class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            lastEle = nums.pop()
            nums[0:0] = [lastEle]
            