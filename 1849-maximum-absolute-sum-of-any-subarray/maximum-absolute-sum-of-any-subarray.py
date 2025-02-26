class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx = float('-inf')
        mn = float('inf')
        cs1 = 0
        cs2 = 0
        for x in nums:
            cs1 = max(x, cs1 + x)
            mx = max(mx, cs1)
            cs2 = min(x, cs2 + x)
            mn = min(mn, cs2)
        return max(abs(mx), abs(mn))