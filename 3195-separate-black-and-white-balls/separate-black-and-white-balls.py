class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        total_count = 0
        left_one_index = 0
        while left_one_index < n and s[left_one_index] != "1":
            left_one_index += 1
        for i in range(left_one_index, n):
            if s[i] == "0":
                total_count += i - left_one_index
                left_one_index += 1
        return total_count
