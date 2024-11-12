class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        c = Counter(words[0])
        for w in words[1:]:
            c &= Counter(w)
        res = []
        for ch, cnt in c.items():
            res.extend([ch] * cnt)
        return res