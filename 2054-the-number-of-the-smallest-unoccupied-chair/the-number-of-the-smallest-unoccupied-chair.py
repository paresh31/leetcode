from collections import *
class Solution:
    def smallestChair(self, times: List[List[int]], tf: int) -> int:
        ev = [(t[0], f) for f, t in enumerate(times)] + [(t[1], -f) for f, t in enumerate(times)]
        ev.sort()
        avail = list(range(len(times)))
        st = dict()
        for t, f in ev:
            f = abs(f)
            if f == tf:
                return heappop(avail)
            if f in st:
                heappush(avail, st[f])
                del st[f]
            else:
                st[f] = heappop(avail)

        