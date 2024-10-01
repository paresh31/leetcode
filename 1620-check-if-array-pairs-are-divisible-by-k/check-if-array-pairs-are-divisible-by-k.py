class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem_count = [0] * k
        for num in arr:
            rem = num % k
            rem_count[rem] += 1
        for i in range(1, k // 2 + 1):
            if rem_count[i] != rem_count[k - i]:
                return False
        if rem_count[0] % 2 != 0:
            return False
        return True

