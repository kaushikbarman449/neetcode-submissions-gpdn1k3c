class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def canShip(capacity):
            currLoad = 0
            daysUsed = 1
            for weight in weights:
                if currLoad + weight > capacity:
                    daysUsed += 1
                    currLoad = weight
                else:
                    currLoad += weight
            
            return daysUsed <= days


        while low < high:
            mid = (low + high) // 2

            if canShip(mid):
                high = mid
            else:
                low = mid + 1
        
        return low