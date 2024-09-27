class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = heights.copy()
        l.sort(reverse=True)
        n = []
        for item in l:
            a = heights.index(item)
            n.append(names[a])
            heights[a] = -1
        return(n)