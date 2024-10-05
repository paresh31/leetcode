class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        c1, c2 = [0] * 26, [0] * 26
        for i in range(m):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
        for i in range(m, n):
            if c1 == c2:
                return True
            c2[ord(s2[i]) - ord('a')] += 1
            c2[ord(s2[i - m]) - ord('a')] -= 1
        return c1 == c2