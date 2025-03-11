class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a': 0, 'b': 0, 'c': 0}
        l, c = 0, 0
        for r in range(len(s)):
            d[s[r]] += 1
            while all(d.values()):
                d[s[l]] -= 1
                l += 1            
            c += l
        return c