class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        stack = [""]
        while stack:
            curr = stack.pop()
            if len(curr) == n:
                res.append(curr)
                if len(res) == k:
                    return curr
                continue
            for c in "cba":
                if not curr or curr[-1] != c:
                    stack.append(curr + c)
        return ""