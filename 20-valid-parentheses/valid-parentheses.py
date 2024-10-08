class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for item in s:
            if len(stack) == 0:
                stack.append(item)
                continue
            if item == ")" and stack[-1] == "(":
                stack.pop()
            elif item == "]" and stack[-1] == "[":
                stack.pop()
            elif item == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(item)
        return True if len(stack) == 0 else False
            
        