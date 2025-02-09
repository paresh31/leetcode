class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if j-i != nums[j] - nums[i]:
        #             c += 1
        # return c

        tot = n * (n - 1) // 2
        freq = {}
        for i, num in enumerate(nums):
            diff = num - i
            if diff in freq:
                c += freq[diff]
                freq[diff] += 1
            else:
                freq[diff] = 1
        return tot - c
        