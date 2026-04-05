class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSq = 1
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                sqLen = 1
                while num + sqLen in numSet:
                    sqLen += 1
                    longestSq = max(longestSq, sqLen)
        
        return 0 if len(nums) == 0 else longestSq