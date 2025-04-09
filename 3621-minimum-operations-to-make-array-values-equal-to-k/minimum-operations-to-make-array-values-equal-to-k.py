class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        count = 0
        for num in nums:
            if num > k and num not in seen:
                seen.add(num)
                count += 1
            if num < k:
                return -1
        return count