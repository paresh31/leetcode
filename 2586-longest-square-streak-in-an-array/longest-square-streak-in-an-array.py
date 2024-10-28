class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        num_set = set(nums)
        max_length = 0
        for num in nums:
            current_length = 1
            current_num = num
            while True:
                next_num = current_num ** 2
                if next_num in num_set:
                    current_length += 1
                    current_num = next_num
                else:
                    break
            if current_length >= 2:
                max_length = max(max_length, current_length)
        return max_length if max_length >= 2 else -1