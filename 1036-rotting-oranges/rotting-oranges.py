class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        r, c = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        t = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y, tm = q.popleft()
            t = max(t, tm)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((nx, ny, tm + 1))
        return -1 if fresh > 0 else t