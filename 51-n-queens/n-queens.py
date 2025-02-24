class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        c = set()
        p = set()
        ne = set()
        res = []
        b = [["."] * n for _ in range(n)]
        def bt(r):
            if r == n:
                res.append(["".join(row) for row in b])
                return
            for col in range(n):
                if col in c or (r + col) in p or (r - col) in ne:
                    continue
                c.add(col)
                p.add(r + col)
                ne.add(r - col)
                b[r][col] = "Q"
                bt(r + 1)
                c.remove(col)
                p.remove(r + col)
                ne.remove(r - col)
                b[r][col] = "."
        bt(0)
        return res