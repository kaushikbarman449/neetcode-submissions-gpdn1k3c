class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_value = {}
        for index, value in enumerate(nums):
            if target - value in index_value:
                return [index_value[target - value], index]
            index_value[value] = index