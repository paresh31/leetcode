class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def dec(k) :
            s=0
            for i in range(k) : s+=code[i]
            ans[-1]=s
            i=0
            j=k
            while i<n-1 :
                if j==n : j=0
                s-=code[i]
                s+=code[j]
                ans[i]=s
                i+=1
                j+=1
            return ans        
        n=len(code)
        ans=[0]*n
        if k==0 : return ans
        elif k>0 :
            return dec(k) 
        else :
            k=-k
            ans = dec(k)
            rotate=n-k-1
            if rotate!=0 : rotate=rotate%n
            return ans[rotate:]+ans[:rotate]