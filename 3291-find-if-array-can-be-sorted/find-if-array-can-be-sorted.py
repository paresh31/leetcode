class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits = [[nums[0]]]
        for i in range(1, len(nums)):
            if bin(bits[-1][-1]).count('1') == bin(nums[i]).count('1'):
                bits[-1].append(nums[i])
            else:
                bits.append([nums[i]])
        for i in range(len(bits)):
            bits[i].sort()        
        flatten = sum(bits, [])
        print(flatten)
        for i in range(len(flatten)-1):
            if flatten[i] <= flatten[i+1]:
                continue
            else:
                return False
        return True