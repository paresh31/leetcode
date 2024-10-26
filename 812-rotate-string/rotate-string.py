class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            temp_string = s[i:] + s[:i]
            if temp_string == goal:
                return True
        return False
