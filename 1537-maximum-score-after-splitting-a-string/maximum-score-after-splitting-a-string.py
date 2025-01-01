class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = left_ones = max_score = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                left_ones += 1
            max_score = max(max_score, zeros + (ones - left_ones))
        return max_score
        