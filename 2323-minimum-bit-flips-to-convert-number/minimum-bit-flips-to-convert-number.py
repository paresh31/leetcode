class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        less = min(start, goal)
        more = max(start, goal)
        bm = bin(more)[2:]
        bl = bin(less)[2:]
        ma = max(len(bm), len(bl))
        mi = min(len(bm), len(bl))
        rl = bl[::-1]
        for i in range(ma-mi):
            rl += "0"
        rl = rl[::-1]
        c = 0
        for i in range(len(bm)):
            if bm[i] != rl[i]:
                c += 1
        return(c)

