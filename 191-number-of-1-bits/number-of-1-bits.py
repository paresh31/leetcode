class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        count = 0
        for item in b:
            if item == "1":
                count += 1
        return count