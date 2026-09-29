class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort the lists
        g.sort()
        s.sort()

        # two pointers, l points to g and r points to s
        l, r = 0, 0

        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                l += 1
            r += 1
        
        return l