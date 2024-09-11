class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        less = min(start, goal)
        more = max(start, goal)
        bs = bin(start)[2:]
        bg = bin(goal)[2:]
        ma = max(len(bs), len(bg))
        mi = min(len(bs), len(bg))
        bm = bin(more)[2:]
        bl = bin(less)[2:]
        rl = bl[::-1]
        for i in range(ma-mi):
            rl += "0"
        rl = rl[::-1]
        c = 0
        for i in range(len(bm)):
            if bm[i] != rl[i]:
                c += 1
        return(c)

