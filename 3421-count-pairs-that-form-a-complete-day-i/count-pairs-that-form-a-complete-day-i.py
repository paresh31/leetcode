class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # c = 0 
        # for i in range(len(hours)-1):
        #     for j in range(i+1, len(hours)):
        #         if (hours[i] + hours[j]) % 24 == 0:
        #             c+=1
        # return c


        r = [0] * 24
        c = 0

        for h in hours:
            rem = h % 24
            comp = (24 - rem) % 24
            c += r[comp]
            r[rem] += 1

        return c