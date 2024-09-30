class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # si = indices.copy()
        # si.sort()
        # ans = ""
        # for i in range(len(s)):
        #     ans += (s[indices.index(i)])
        # return ans
        n = len(s)
        el = ['']*n
        for i in range(n):
            el[indices[i]] = s[i]
        return ''.join(el)
