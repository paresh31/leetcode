class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        stack = [(1, [])]
        while stack:
            start, path = stack.pop()
            if len(path) == k:
                result.append(path)
            else:
                for i in range(start, n + 1):
                    stack.append((i + 1, path + [i]))
        return result