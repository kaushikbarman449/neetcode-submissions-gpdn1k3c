class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        freqT = {}
        for ch in t:
            if ch in freqT:
                freqT[ch] += 1
            else:
                freqT[ch] = 1

        window = {}
        have, need = 0, len(freqT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1

            if s[r] in freqT and window[s[r]] == freqT[s[r]]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1

                if s[l] in freqT and window[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""