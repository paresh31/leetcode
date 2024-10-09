class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c = 0
        stack = list()
        for i in s:
            if len(stack) == 0 and i == "(":
                stack.append(i)
                continue
            if len(stack) == 0 and i == ")":
                c += 1
                continue
            if i == "(":
                stack.append(i)
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                c += 1
        return len(stack) + c
            
        

        