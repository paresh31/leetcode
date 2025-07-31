class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        act = ord(target) + 1
        li = []
        for item in letters:
            li.append(ord(item))
        if act == 123: return letters[0]
        left = 0
        right = len(li) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if li[mid] >= act:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return letters[res] if res != -1 else letters[0]
        