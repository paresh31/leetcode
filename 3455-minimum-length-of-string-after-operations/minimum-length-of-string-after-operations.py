class Solution:
    def minimumLength(self, s: str) -> int:
        a = [0] * 26
        for c in s:
            a[ord(c) - ord('a')] += 1
        for i in range(26):
            while a[i] >= 3:
                a[i] -= 2
        l = sum(a)
        return l