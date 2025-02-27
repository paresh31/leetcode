class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        r = 0
        n = len(arr)
        for i in range(n - 1):
            for j in range(i +1, n):
                p, c = arr[i], arr[j]
                nxt = p + c
                le = 2
                while nxt in s:
                    le += 1
                    p, c = c, nxt
                    nxt = p + c
                    r = max(r, le)
        return r