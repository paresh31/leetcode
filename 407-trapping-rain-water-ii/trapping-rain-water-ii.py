class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        v = [[False] * n for _ in range(m)]
        h = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(h, (heightMap[i][j], i, j))
                    v[i][j] = True
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        w = 0
        while h:
            ht, x, y = heapq.heappop(h)
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not v[nx][ny]:
                    w += max(0, ht - heightMap[nx][ny])
                    heapq.heappush(h, (max(ht, heightMap[nx][ny]), nx, ny))
                    v[nx][ny] = True
        return w