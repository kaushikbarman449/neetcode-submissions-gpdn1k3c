class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        currentScore = sum(cardPoints[:k])
        max_score = currentScore

        for i in range(k):
            # remove leftmost element
            currentScore -= cardPoints[k - 1 - i]
            # add rightmost element
            currentScore += cardPoints[n - 1 - i]

            max_score = max(max_score, currentScore)

        return max_score