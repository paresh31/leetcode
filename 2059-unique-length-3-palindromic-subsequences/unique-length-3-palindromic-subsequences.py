class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        checked = set()
        a = 0
        for i in range(len(s)):
            u = set()
            if s[i] not in checked:
                for j in range(i + 1, s.rindex(s[i])):
                    u.add(s[j])
                checked.add(s[i])
                a += len(u)
        return a