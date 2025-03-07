class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def ip(n: int) -> bool:
            if n < 2:
                return False
            if n in (2, 3):
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(5, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        arr = []
        for i in range(left, right + 1):
            if ip(i):
                arr.append(i)
        if len(arr) < 2:
            return [-1,-1]
        gaps = []
        for i in range(1,len(arr)):
            g = arr[i] - arr[i-1]
            gaps.append(g)
        first = gaps.index(min(gaps))
        res = [arr[first], arr[first + 1]]
        return res

                