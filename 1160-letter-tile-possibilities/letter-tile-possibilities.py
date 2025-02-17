class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def b(fq):
            c = 0
            for x in fq:
                if fq[x] > 0:
                    c += 1
                    fq[x] -= 1
                    c += b(fq)
                    fq[x] += 1
            return c
        fq = {}
        for x in tiles:
            fq[x] = fq.get(x, 0) + 1
        return b(fq)