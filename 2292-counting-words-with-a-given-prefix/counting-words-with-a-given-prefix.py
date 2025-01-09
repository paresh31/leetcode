class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pl = len(pref)
        count, res = 0, 0
        for word in words:
            if len(word) < pl:
                continue
            else:
                for i in range(pl):
                    if word[i] == pref[i]:
                        count += 1
                if count == pl:
                    res += 1
            count = 0
        return res
