class Solution:

    def _rotateArr(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        self._rotateArr(0, n-1, nums)
        self._rotateArr(0, k -1, nums)
        self._rotateArr(k, n-1, nums)

        return nums


