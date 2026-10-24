class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        window = {}
        left = 0
        right = 0

        while right < len(fruits):
            if fruits[right] in window:
                window[fruits[right]] += 1
            else:
                window[fruits[right]] = 1

            while len(window) > 2:
                window[fruits[left]] -= 1

                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                
                left += 1

            maxFruits = max(maxFruits, right - left + 1)
            right += 1
            
        return maxFruits
