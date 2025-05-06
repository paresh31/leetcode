class Solution:
    def hammingWeight(self, n: int) -> int:
        # b = bin(n)[2:]
        # count = 0
        # for item in b:
        #     if item == "1":
        #         count += 1
        # return count
        count = 0
        while n:
            count += n & 1
            n = n >> 1
        return count