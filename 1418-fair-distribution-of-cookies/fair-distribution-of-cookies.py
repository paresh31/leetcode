class Solution:
    def distributeCookies(self, a: List[int], k: int) -> int:
        n = len(a)
        m = 1 << n
        s = [0] * m
        for mask in range(m):
            for i in range(n):
                if (mask >> i) & 1:
                    s[mask] += a[i]
        dp = [[-1] * (k + 1) for q in range(m)]
        def f(mask, b):
            if b == 0:
                return 0 if mask == 0 else float('inf')
            if dp[mask][b] != -1:
                return dp[mask][b]
            ans = float('inf')
            sub = mask
            while sub:
                rem = mask ^ sub
                val = max(s[sub], f(rem, b - 1))
                ans = min(ans, val)
                sub = (sub - 1) & mask
            dp[mask][b] = ans
            return ans
        return f((1 << n) - 1, k)