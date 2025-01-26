class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        d = [0] * n
        for f in favorite:
            d[f] += 1
        q = deque([i for i in range(n) if d[i] == 0])
        l = [0] * n
        while q:
            x = q.popleft()
            y = favorite[x]
            l[y] = max(l[y], l[x] + 1)
            d[y] -= 1
            if d[y] == 0:
                q.append(y)
        v = [False] * n
        m = 0
        t = 0
        for i in range(n):
            if not v[i] and d[i] > 0:
                s = 0
                x = i
                while not v[x]:
                    v[x] = True
                    x = favorite[x]
                    s += 1
                if s == 2:
                    a, b = i, favorite[i]
                    t += 2 + l[a] + l[b]
                else:
                    m = max(m, s)
        return max(m, t)