class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        n = len(grid)
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y, id):
            s = [(x, y)]
            grid[x][y] = id
            sz = 0
            while s:
                i, j = s.pop()
                sz += 1
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = id
                        s.append((ni, nj))
            return sz
        m = {0: 0}  
        id = 2  
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    m[id] = dfs(i, j, id)
                    id += 1
        mx = max(m.values())  
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    s = set()
                    for di, dj in d:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            s.add(grid[ni][nj])
                    mx = max(mx, 1 + sum(m[x] for x in s))
        return mx