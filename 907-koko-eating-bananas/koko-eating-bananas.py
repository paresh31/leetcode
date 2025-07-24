class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        mn, mx = 1, max(piles)
        ans = mx
        while mn <= mx:
            mid = (mn + mx) // 2
            s = 0
            for item in piles:
                s += math.ceil(item / mid)
            if s <= h:
                ans = mid
                mx = mid -1
            else: 
                mn = mid + 1
        return ans
