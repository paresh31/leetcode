class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a1,a2 = "",""
        for i in word1:
            a1 += i
        for j in word2:
            a2 += j
        return a1 == a2