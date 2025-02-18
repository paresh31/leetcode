class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c = 0
        for word in words:
            le = len(word)
            if s[:le] == word:
                c += 1
        return c