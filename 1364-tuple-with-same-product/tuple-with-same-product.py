class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N=len(nums)
        res=0
        map={}
        for i in range(0,N):
            for j in range(i+1, N):
                prod=nums[i]*nums[j]
                map[prod]=map.get(prod,0)+1
        for key,val in map.items():
            if val>=2:
                res+=8*val*(val-1)/2
        return int(res)