class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pl = len(pref)
        res = 0
        for word in words:
            if len(word) < pl:
                continue
            else:
                count = 0
                for i in range(pl):
                    if word[i] == pref[i]:
                        count += 1
                if count == pl:
                    res += 1
            
        return res
