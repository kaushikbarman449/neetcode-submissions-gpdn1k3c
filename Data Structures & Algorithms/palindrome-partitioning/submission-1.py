class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(strList):
            l = 0
            r = len(strList) - 1
            while l < r:
                if strList[l] != strList[r]:
                    return False
                l += 1
                r -= 1
            return True

        def helper(index, currPartition):
            if index == len(s):
                ans.append(currPartition.copy())
                return

            for j in range(index, len(s)):
                substring = s[index : j + 1]
                if isPalindrome(substring):
                    currPartition.append(substring)
                    helper(j + 1, currPartition)
                    currPartition.pop()
        
        helper(0, [])

        return ans