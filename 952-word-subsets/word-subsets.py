class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        m = {}
        for b in words2:
            t = {}
            for c in b:
                t[c] = t.get(c, 0) + 1
            for c, f in t.items():
                m[c] = max(m.get(c, 0), f)
        r = []
        for a in words1:
            t = {}
            for c in a:
                t[c] = t.get(c, 0) + 1
            if all(t.get(c, 0) >= f for c, f in m.items()):
                r.append(a)
        return r