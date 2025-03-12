class Solution:
    def nearestPalindromic(self, s: str) -> str:
        a = int(s)
        b = len(s)
        if a <= 10:
            return str(a - 1)
        if a == 11:
            return str(9)
        c = set()
        c.add(10**(b - 1) - 1)
        c.add(10**b + 1)
        d = int(s[: (b + 1) // 2])
        for e in (-1, 0, 1):
            f = d + e
            g = str(f)
            if b % 2 == 0:
                h = g + g[::-1]
            else:
                h = g + g[:-1][::-1]
            c.add(int(h))
        c.discard(a)
        i = None
        j = float('inf')
        for k in c:
            m = abs(k - a)
            if m < j or (m == j and k < i):
                j = m
                i = k
        return str(i)