class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tc = sum(chalk)
        k %= tc
        for i, cn in enumerate(chalk):
            if k < cn:
                return i
            k -= cn
