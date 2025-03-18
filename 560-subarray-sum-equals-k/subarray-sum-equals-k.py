class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     s = nums[i]
        #     if s == k:
        #         count += 1
        #     for j in range(i+1, len(nums)):
        #         s += nums[j]
        #         if s == k:
        #             count += 1
        # return count

        pc = {0:1}
        ps = 0
        c = 0
        for n in nums:
            ps += n
            if ps - k in pc:
                c += pc[ps - k]
            if ps in pc:
                pc[ps] += 1
            else:
                pc[ps] = 1
        return c
                
                
                