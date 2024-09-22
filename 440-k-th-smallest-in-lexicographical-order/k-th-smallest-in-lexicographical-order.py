class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def cnt(p, n):
            s = 0
            c = p
            nxt = p + 1
            while c <= n:
                s += min(n + 1, nxt) - c
                c *= 10
                nxt *= 10
            return s
        cur = 1
        k -= 1
        while k > 0:
            s = cnt(cur, n)
            if s <= k:
                cur += 1
                k -= s
            else:
                cur *= 10
                k -= 1
        return cur
        