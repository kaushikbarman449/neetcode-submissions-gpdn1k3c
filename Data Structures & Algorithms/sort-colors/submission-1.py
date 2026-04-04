class Solution:

    def partition(self, nums, low, high):
        pivot = nums[low]
        i = low
        j = high

        while i < j:
            while i <= high and nums[i] <= pivot:
                i += 1
            while j >= low and nums[j] > pivot:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[low], nums[j] = nums[j], nums[low]

        return j

    def quick_sort(self, nums, low, high):
        if low < high:
            j = self.partition(nums, low, high)
            self.quick_sort(nums, low, j - 1)
            self.quick_sort(nums, j + 1, high)
        return nums

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.quick_sort(nums, 0, len(nums) - 1)

        