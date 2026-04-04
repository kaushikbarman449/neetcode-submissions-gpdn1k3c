class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writePos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[writePos] = nums[writePos], nums[i]
                writePos += 1
        return nums
        