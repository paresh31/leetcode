class Solution:
    def thousandSeparator(self, n: int) -> str:
        ns = str(n)
        l = len(ns)
        if l < 4 :
            return ns
        res = ""
        ns = ns[::-1]
        for i in range(l) :
            if not i % 3 and i != 0 :
                res += "."
            res += ns[i]
        return res[::-1]