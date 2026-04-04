class Solution:

    def merge(self, first: int, second: int) -> List[int]:
        i, j, final = 0, 0, []
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1        
        while i < len(first):
            final.append(first[i])
            i += 1
        while j < len(second):
            final.append(second[j])
            j += 1
        return final

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        first = self.sortArray(nums[: len(nums) // 2])
        second = self.sortArray(nums[len(nums) // 2:])

        return self.merge(first, second)