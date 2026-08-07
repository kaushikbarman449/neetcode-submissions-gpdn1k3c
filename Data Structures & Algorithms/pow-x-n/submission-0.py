class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            half = power(x, n // 2)
            return x * half * half if n % 2 else half * half 

        # handle negative powers
        if n < 0:
            x = 1 / x
            n = -n
        
        return power(x, n)
        