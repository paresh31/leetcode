class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a = list(map(str, nums))
        a.sort(key = lambda x: x*10, reverse=True)
        l = ''.join(a)
        if a[0] == "0":
            return("0")
        return(l)