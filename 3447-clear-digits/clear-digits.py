class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                while stack and stack[-1].isdigit():
                    stack.pop()
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
