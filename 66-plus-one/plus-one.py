class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = ""
        for i in range(len(digits)):
            c += str(digits[i])
        a = str(int(c)+1)
        b = list(a)
        l = []
        for item in b:
            l.append(int(item))
        return l