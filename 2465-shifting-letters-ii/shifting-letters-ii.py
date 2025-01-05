class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = [0] * (n + 1)        
        for a, b, c in shifts:
            x = 1 if c == 1 else -1
            d[a] += x
            d[b + 1] -= x
        p = [0] * n
        t = 0
        for i in range(n):
            t += d[i]
            p[i] = t
        r = []
        for i, ch in enumerate(s):
            shift = p[i] % 26
            r.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        return ''.join(r)