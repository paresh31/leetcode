class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        if  k > len(s):
            k = k % len(s)
        r = s[k:]
        r += s[:k]
        return r