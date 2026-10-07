class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # keep track of farthest you can reach
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
    
        return True
