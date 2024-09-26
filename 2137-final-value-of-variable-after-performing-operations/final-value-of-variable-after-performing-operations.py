class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        r = 0
        for item in operations:
            if item == "--X" or item == "X--":
                r -= 1
            elif item == "++X" or item == "X++":
                r += 1
        return r

        