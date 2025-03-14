class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        l, r = 1, max(candies)
        res = 0
        while l <= r:
            m = (l + r) // 2
            count = 0 
            for x in candies:
                count += x // m
            if count >= k:
                res = m 
                l = m + 1 
            else:
                r = m - 1 
        return res