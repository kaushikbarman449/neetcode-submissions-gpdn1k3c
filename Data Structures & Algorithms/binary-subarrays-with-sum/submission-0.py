class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # count num of subarrays with currSum <= x
        def helper(x):
            if x < 0: return 0

            subArrs = 0
            r, l = 0, 0
            currSum = 0
            for r in range(len(nums)):
                currSum += nums[r]

                while currSum > x:
                    currSum -= nums[l]
                    l += 1
                
                subArrs += (r - l + 1)
            return subArrs

        return helper(goal) - helper(goal - 1)
