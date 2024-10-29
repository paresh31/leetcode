class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1, r2, r3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for w in words:
            lw = set(w.lower())
            if lw.issubset(r1) or lw.issubset(r2) or lw.issubset(r3):
                res.append(w)
        return res