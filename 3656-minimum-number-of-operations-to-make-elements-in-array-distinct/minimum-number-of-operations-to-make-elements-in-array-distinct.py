class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = len(nums)
        c = 0
        for i in range(0, len(nums), 3):
            if len(set(nums[i:])) == l-i:
                break
            else:
                c += 1
        return c