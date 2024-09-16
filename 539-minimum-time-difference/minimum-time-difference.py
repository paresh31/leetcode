class Solution:
    def findMinDifference(self, tp: List[str]) -> int:
        mins = []
        for t in tp:
            h, m = int(t[:2]), int(t[3:])
            mins.append(h * 60 + m)
        mins.sort()
        min_diff = float('inf')
        for i in range(1, len(mins)):
            min_diff = min(min_diff, mins[i] - mins[i - 1])
        min_diff = min(min_diff, (1440 + mins[0] - mins[-1]))
        return(min_diff)
