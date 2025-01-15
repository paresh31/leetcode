class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_set_bits(n):
            return bin(n).count('1')
        set_bits_num2 = count_set_bits(num2)
        x = 0
        for i in range(31, -1, -1):
            if set_bits_num2 == 0:
                break
            if num1 & (1 << i):
                x |= (1 << i)
                set_bits_num2 -= 1
        for i in range(32):
            if set_bits_num2 == 0:
                break
            if not (x & (1 << i)):
                x |= (1 << i)
                set_bits_num2 -= 1
        return x
