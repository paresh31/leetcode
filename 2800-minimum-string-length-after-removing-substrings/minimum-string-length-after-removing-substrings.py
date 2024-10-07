class Solution:
    def minLength(self, s: str) -> int:
        arr = list()
        for item in s:
            if len(arr) == 0:
                arr.append(item)
                continue
            if item == "B" and arr[-1] == "A":
                arr.pop()
            elif item == "D" and arr[-1] == "C":
                arr.pop()
            else:
                arr.append(item)
        return len(arr)





        # res =  0
        # for i in range(len(s)-1):
        #     if (s[i] == "A" and s[i+1] == "B") or (s[i] == "C" and s[i+1] == "D"):
        #         res += 2
        # return len(s) - res
        