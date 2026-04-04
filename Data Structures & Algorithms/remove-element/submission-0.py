class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writePos = 0
        readPos = 0
        while readPos < len(nums):
            if nums[readPos] != val:
                if nums[readPos] != nums[writePos]:
                    nums[writePos] = nums[readPos]
                writePos += 1
                readPos += 1
            else:
                readPos += 1
        return writePos