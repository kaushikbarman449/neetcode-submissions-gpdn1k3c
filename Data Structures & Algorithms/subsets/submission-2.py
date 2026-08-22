class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):            # check if the bit is set in mask's ith position
                    subset.append(nums[i])
            
            ans.append(subset)
        return ans