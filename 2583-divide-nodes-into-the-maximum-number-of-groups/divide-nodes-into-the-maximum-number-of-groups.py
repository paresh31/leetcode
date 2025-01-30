class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        from collections import deque
        def bp(u, c):
            clr[u] = c
            cmp.append(u)
            for v in g[u]:
                if (not clr[v] and not bp(v, -1 * c)) or clr[v] == c:
                    return False
            return True

        def fd(r):
            vis = [0] * n
            q, vis[r], d = deque([r]), 1, 0
            while q:
                for _ in range(len(q)):
                    for v in g[q.popleft()]:
                        if not vis[v]:
                            q.append(v)
                            vis[v] = 1
                d += 1
            return d

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v - 1].append(u - 1)
            g[u - 1].append(v - 1)

        res, clr = 0, [0] * n
        for u in range(n):
            if not clr[u]:
                cmp = []
                if not bp(u, 1):
                    return -1
                res += max(fd(u) for u in cmp)
        return res