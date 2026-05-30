# Time complexity: O(n + m)
# Space complexity: O(n + m)

class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        x, y = 0, 0
        mergedArr = []

        while x < len(arr1) and y < len(arr2):
            if arr1[x] <= arr2[y]:
                mergedArr.append(arr1[x])
                x += 1
            else:
                mergedArr.append(arr2[y])
                y += 1

        while y < len(arr2):
            mergedArr.append(arr2[y])
            y += 1

        while x < len(arr1):
            mergedArr.append(arr1[x])
            x += 1

        mid = len(mergedArr) // 2

        if len(mergedArr) % 2 == 0:
            return (mergedArr[mid - 1] + mergedArr[mid]) / 2
        else:
            return mergedArr[mid]