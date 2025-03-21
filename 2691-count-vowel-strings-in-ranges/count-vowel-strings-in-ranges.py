class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        valid = list()
        for word in words:
            valid.append(1 if word[0] in vowels and word[-1] in vowels else 0)
        prefix = [0]
        for count in valid:
            prefix.append(prefix[-1] + count)
        result = list()
        for li, ri in queries:
            result.append(prefix[ri+1] - prefix[li])
        return result

