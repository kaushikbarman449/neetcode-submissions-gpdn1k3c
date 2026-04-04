class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        k = 0
        mergedStr = []
        while k < len(word1) + len(word2):
            while i < len(word1):
                mergedStr.append(word1[i])
                break
            while j < len(word2):
                mergedStr.append(word2[j])
                break
            i += 1
            j += 1
            k += 1
        return ''.join(mergedStr)