class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        li = list()
        skill.sort()
        begining = 0
        ending = -1
        for i in range(len(skill)//2):
            li.append([skill[begining], skill[ending]])
            begining += 1
            ending -= 1
        for i in range(len(li)-1):
            if sum(li[i]) != sum(li[i+1]):
                return -1
        sm = 0
        for i in range(len(li)):
            m = li[i][0] * li[i][1]
            sm += m
        return sm 