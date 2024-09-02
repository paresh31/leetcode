class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tc = sum(chalk)
        k %= tc
        c = 0
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                break
            c += 1
        return(c % len(chalk))