class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # expected = set(range(1, len(nums) + 1))
        # actual = set(nums)
        # return list(expected - actual)
        s = set(nums)
        r = []
        for i in range(1, len(nums)+1):
            if i not in s:
                r.append(i)
        return r
