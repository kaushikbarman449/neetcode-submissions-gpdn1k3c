class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        finalMerge = []
        intervals.sort(key = lambda x : x[0])

        start, end = intervals[0]

        for i in range(len(intervals)):
            s, e = intervals[i]

            if s <= end:
                end = max(e, end)
            else:
                finalMerge.append([start, end])
                start, end = s, e

        finalMerge.append([start, end])
        return finalMerge

