class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        result = [0] * len(nums)

        for k in range(len(nums)):
            if k % 2 == 0:
                while nums[i] < 0:
                    i += 1
                result[k] = nums[i]
                i += 1
            else:
                while nums[j] > 0:
                    j += 1
                result[k] = nums[j]
                j += 1
        return result