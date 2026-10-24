class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        numZeroes = 0
        longestSeq = 0

        while right < len(nums):
            if nums[right] == 0:
                numZeroes += 1
            
            while numZeroes == 2:
                if nums[left] == 0:
                    numZeroes -= 1
                left += 1


            longestSeq = max(longestSeq, right - left + 1)
            right += 1
        
        return longestSeq

# nums = [1, 1, 1, 0, 0, 1, 1]