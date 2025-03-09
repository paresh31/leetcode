class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l,r = 0,len(colors)
        res = 0
        win_len = 1 
        while l<r:
            for i in range(k-win_len):
                if colors[(l+win_len-1)%r] == colors[(l+win_len)%r]:
                    l += win_len
                    win_len = 1
                    break
                win_len+=1
            if win_len==k:
                res+=1
                l+=1
                win_len-=1
        return res