class Solution:
    def reverseWords(self, s: str) -> str:
        splited_s = s.split()
        empty_list = list()
        for word in splited_s:
            word = word[::-1]
            empty_list.append(word)
        return ' '.join(empty_list)

        