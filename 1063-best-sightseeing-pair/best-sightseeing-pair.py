class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi = 0
        best_i = values[0]
        for j in range(1, len(values)):
            maxi = max(maxi, best_i + values[j] - j)
            best_i = max(best_i, values[j] + j)
        return maxi