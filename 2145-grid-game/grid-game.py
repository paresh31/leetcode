class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        a = [0] * n
        b = [0] * n
        a[0] = grid[0][0]
        b[0] = grid[1][0]
        for i in range(1, n):
            a[i] = a[i - 1] + grid[0][i]
            b[i] = b[i - 1] + grid[1][i]
        t = a[-1]
        u = b[-1]
        m = float('inf')
        for i in range(n):
            x = t - a[i]
            y = b[i - 1] if i > 0 else 0
            z = max(x, y)
            m = min(m, z)
        return m