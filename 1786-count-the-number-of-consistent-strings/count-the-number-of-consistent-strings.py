class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a_set = set(allowed)
        c = 0
        for word in words:
            if all(char in a_set for char in word):
                c += 1
                
        return c
