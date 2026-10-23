class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_stop = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                return jumps + 1
            
            if i == current_stop:
                jumps += 1
                current_stop = farthest
        
        return jumps