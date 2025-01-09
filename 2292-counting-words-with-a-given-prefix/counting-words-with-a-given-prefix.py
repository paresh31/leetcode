class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pl = len(pref)
        res = 0
        for word in words:
            count = 0
            if len(word) < pl:
                continue
            else:
                for i in range(pl):
                    if word[i] == pref[i]:
                        count += 1
                if count == pl:
                    res += 1 
        return res
