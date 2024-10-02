class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        d = {}
        rank = 1
        for item in sorted_unique:
            d[item] = rank
            rank += 1
        ranked_list = list()
        for item in arr:
            ranked_list.append(d[item])
        return ranked_list
        