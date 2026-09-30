class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False

        count_5s = 0
        count_10s = 0

        for bill in bills:
            if bill == 5:
                count_5s += 1
            elif bill == 10:
                if count_5s == 0:
                    return False

                count_5s -= 1
                count_10s += 1
            else:
                # $10 + $5
                if (count_10s > 0 and count_5s > 0):
                    count_5s -= 1
                    count_10s -= 1
                elif count_5s >= 3:                     # three $5 bills
                    count_5s -= 3
                else:
                    return False

        return True