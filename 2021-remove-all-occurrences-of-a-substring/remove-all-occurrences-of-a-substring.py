class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = list()
        le = len(part)
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= len(part):
                temp = ''.join(stack)
                if temp[-le:] == part:
                    del stack[-le:]
        return ''.join(stack)
        