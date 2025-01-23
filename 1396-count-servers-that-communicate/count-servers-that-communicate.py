class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r = [0] * m
        c = [0] * n        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r[i] += 1
                    c[j] += 1        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if r[i] > 1 or c[j] > 1:
                        res += 1        
        return res