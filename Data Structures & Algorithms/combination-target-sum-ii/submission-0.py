class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # since the list contains duplicates
        candidates.sort()

        def helper(i, k, currList):
            # Base case
            if k == 0:
                ans.append(list(currList))
                return

            if k < 0 or i == len(candidates):
                return

            # include candidates[i]
            helper(i + 1, k - candidates[i], currList + [candidates[i]])

            # skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, k, currList)    


        helper(0, target, [])
        return ans