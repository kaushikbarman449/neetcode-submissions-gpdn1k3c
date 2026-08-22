class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(index, currList):
            if index == len(nums):
                ans.append(currList.copy())
                return

            # Choice 1: take the index
            helper(index + 1, currList)

            # choice 2: don't take the index
            currList.append(nums[index])
            helper(index + 1, currList)
            currList.pop()


        helper(0, [])

        return ans