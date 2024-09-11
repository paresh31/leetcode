class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = ""
        for i in range(len(digits)):
            c += str(digits[i])
        a = int(c)+1
        b = str(a)
        l = list()
        for i in range(len(b)):
            l.append(int(b[i]))
        return l