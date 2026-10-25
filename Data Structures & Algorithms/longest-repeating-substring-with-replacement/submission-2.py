class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        longestSq = 0
        maxFreq = 0
        window = {}

        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1
            
            maxFreq = max(maxFreq, window[s[right]])
            
            # invariant
            while (right - left + 1) - maxFreq > k:
                window[s[left]] -= 1
                left += 1


            longestSq = max(longestSq, right - left + 1)
            right += 1
        

        return longestSq