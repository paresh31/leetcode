class Solution:
    def decodeString(self, s: str) -> str:
        st, n, res = [], 0, ""
        for ch in s:
            if ch.isdigit():
                n = n * 10 + int(ch)
            elif ch == '[':
                st.append((res, n))
                res, n = "", 0
            elif ch == ']':
                p, x = st.pop()
                res = p + x * res
            else:
                res += ch
        return res