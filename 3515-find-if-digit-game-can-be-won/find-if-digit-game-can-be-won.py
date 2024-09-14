class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        ones, tens = [],[]
        for i in nums:
            if i > 0 and i < 10:
                ones.append(i)
            elif i >= 10 and i < 100:
                tens.append(i)
        tot_sum = sum(nums)
        so = sum(ones)
        st = sum(tens)
        if (tot_sum - so < so) or (tot_sum - st < st):
            return True
        return False