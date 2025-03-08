class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        t = len(blocks) - k + 1
        c_arr = []
        for i in range(t):
            arr = blocks[i:i+k].count('W')
            c_arr.append(arr)
        return min(c_arr)

        