class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        m = 10**9 + 7
        o = 0
        e = 1
        s = 0
        r = 0
        for x in arr:
            s += x
            if s % 2:
                r += e
                o += 1
            else:
                r += o
                e += 1
            r %= m
        return r
                
