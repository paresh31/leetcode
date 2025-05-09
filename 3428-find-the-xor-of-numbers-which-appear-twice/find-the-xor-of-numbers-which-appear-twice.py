class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count = {}
        for item in nums:
            count[item] = count.get(item, 0) + 1
        result = 0
        for num, freq in count.items():
            if freq == 2:
                result ^= num
        return result