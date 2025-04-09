class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(x < k for x in nums):
            return -1
        seen = set()
        count = 0
        for num in nums:
            if num > k and num not in seen:
                seen.add(num)
                count += 1
        return count