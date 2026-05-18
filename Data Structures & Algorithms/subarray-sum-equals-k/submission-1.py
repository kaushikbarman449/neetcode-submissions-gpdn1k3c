class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_count = 0 

        prefixSum = 0
        prefixSumMap = {}
        prefixSumMap[0] = 1

        for i in range(n):
            prefixSum += nums[i]
            prefL = prefixSum - k
            if prefL in prefixSumMap:
                total_count += prefixSumMap[prefL]
            
            if prefixSum in prefixSumMap:
                prefixSumMap[prefixSum] += 1
            else:
                prefixSumMap[prefixSum] = 1
        
        return total_count
