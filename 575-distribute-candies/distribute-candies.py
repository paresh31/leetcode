class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        s = len(set(candyType))
        r = n // 2
        return min(s, r)