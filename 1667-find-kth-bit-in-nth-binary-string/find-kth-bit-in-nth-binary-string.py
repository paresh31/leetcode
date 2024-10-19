class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s1 = '0'
        for i in range(n-1):
            com = ''.join('1' if bit == '0' else '0' for bit in s1)
            rev_com = com[::-1]
            s1 = s1 + '1' + rev_com
        return s1[k-1]