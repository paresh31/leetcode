class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        i, j = 0, 0
        while i < n and j < m:
            c1, c2 = str1[i], str2[j]
            if c1 == c2:
                i += 1
                j += 1
            elif (ord(c2) - ord(c1)) % 26 <= 1:
                i += 1
                j += 1
            else:
                i += 1
        return j == m