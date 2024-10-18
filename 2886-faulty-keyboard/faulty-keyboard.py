class Solution:
    def finalString(self, s: str) -> str:
        emchar = ""
        for char in s:
            if char != 'i':
                emchar += char
            else:
                emchar = emchar[::-1]
        return emchar
        