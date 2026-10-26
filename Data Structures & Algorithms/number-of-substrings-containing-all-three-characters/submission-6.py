class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, right, substrings = 0, 0, 0
        freq = {}
        while right < len(s):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            if freq.get('a', 0) >= 1 and freq.get('b', 0) >= 1 and freq.get('c', 0) >= 1:
                while freq.get('a', 0) >= 1 and freq.get('b', 0) >= 1 and freq.get('c', 0) >= 1:
                    substrings += len(s) - right
                    freq[s[left]] -= 1
                    left += 1
            right += 1
        
        return substrings