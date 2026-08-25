class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        
        for x in nums:          # first we xor everything
            xor ^= x            # xor = 3 ^ 5
        
        mask = xor & -xor       # gives the rightmost set bit

        a, b = 0, 0             # split nums into groups according to the rightmost set bit
        
        for x in nums:
            if x & mask:
                a ^= x
            else:
                b ^= x

        return [a, b]