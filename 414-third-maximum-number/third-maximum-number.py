class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = float('-inf')
        for n in nums:
            if n in (m1, m2, m3): continue
            if n > m1: m3, m2, m1 = m2, m1, n
            elif n > m2 and n < m1: m3, m2 = m2, n
            elif n > m3 and n < m2: m3 = n
        return m3 if m3 != float('-inf') else m1