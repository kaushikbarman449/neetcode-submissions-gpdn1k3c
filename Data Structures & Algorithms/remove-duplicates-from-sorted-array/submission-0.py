class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writePos = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[writePos]:
                writePos += 1
            nums[i], nums[writePos] = nums[writePos], nums[i]
        return writePos + 1