class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for i in range(len(sentences)):
            sentences[i] = sentences[i].split()
            mx = max(len(sentences[i]), mx)
        return mx