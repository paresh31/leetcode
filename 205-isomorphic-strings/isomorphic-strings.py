class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m_st = {}
        m_ts = {}
        for a, b in zip(s, t):
            if a in m_st:
                if m_st[a] != b:
                    return False
            else:
                m_st[a] = b
            if b in m_ts:
                if m_ts[b] != a:
                    return False
            else:
                m_ts[b] = a
        return True