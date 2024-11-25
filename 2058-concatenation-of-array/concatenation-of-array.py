class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        emt_list = [0]*(2*l)
        for i in range(l):
            temp = nums[i]
            emt_list[i] = temp
            emt_list[l + i] = temp
        return emt_list
