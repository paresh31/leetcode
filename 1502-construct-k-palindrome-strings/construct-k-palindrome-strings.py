class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        elif k == n or k >= 26:
            return True
        else:
            single_dict = {}
            for ch in s:
                if ch in single_dict:
                    single_dict.pop(ch)
                else:
                    single_dict[ch] = None

            if k < len(single_dict):
                return False
            else:
                return True 