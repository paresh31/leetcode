class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # d = {}
        # for i in nums:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # for v in d.values():
        #     if v > 1:
        #         return True
        # return False

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]: return True
        return False