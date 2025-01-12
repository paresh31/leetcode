class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        b, f = 0, 0
        for i in range(n):
            if locked[i] == '0':
                f += 1
            else:
                b += 1 if s[i] == '(' else -1
            if b + f < 0:
                return False
        b, f = 0, 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':
                f += 1
            else:
                b += 1 if s[i] == ')' else -1
            if b + f < 0:
                return False
        return True