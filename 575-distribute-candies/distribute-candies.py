class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        # r = n // 2
        # return min(s, r)
        d = dict()
        for item in candyType:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        d_len = len(d)
        return min(n // 2, d_len)
        