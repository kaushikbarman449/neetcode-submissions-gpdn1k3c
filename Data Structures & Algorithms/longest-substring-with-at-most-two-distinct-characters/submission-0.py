class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longestSq = 0
        left = right = 0
        
        window = {}

        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            while len(window) > 2:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1    

            longestSq = max(longestSq, right - left + 1)
            right += 1
        
        return longestSq