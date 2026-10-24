class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currentScore = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                currentScore += 1
                maxOnes = max(maxOnes, currentScore)
            else:
                currentScore = 0

        return maxOnes