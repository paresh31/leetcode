class Solution:
    def minSwaps(self, s: str) -> int:
        c, mx = 0, 0
        for item in s:
            if item == "[":
                c -= 1
            else:
                c += 1
            mx = max(c, mx)
        return (mx + 1) // 2