class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        x, y = 0, 0

        total_len = len(arr1) + len(arr2)
        mid = total_len // 2

        prev, curr = 0, 0  # to handle if total_len is even

        for _ in range(mid + 1):

            prev = curr

            if x < len(arr1) and y < len(arr2):
                if arr1[x] <= arr2[y]:
                    curr = arr1[x]
                    x += 1
                else:
                    curr = arr2[y]
                    y += 1
            elif x < len(arr1):
                curr = arr1[x]
                x += 1
            else:
                curr = arr2[y]
                y += 1

        if total_len % 2:
            return curr

        return (prev + curr) / 2