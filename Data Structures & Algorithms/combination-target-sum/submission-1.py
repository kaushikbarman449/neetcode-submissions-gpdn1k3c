class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(index, k, currList):

            if k == 0:
                ans.append(list(currList))
                return
            
            if k < 0 or index == len(nums):
                return
            
            # choice 1: Include
            currList.append(nums[index])
            helper(index, k - nums[index], currList)
            currList.pop()


            # choice 2: Exclude
            helper(index + 1, k, currList)

        
        helper(0, target, [])

        return ans