class Solution:
    def __init__(self):
        self.longest = ''
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        map = {'a':a, 'b':b, 'c':c}
        def bt(map, tmp):
            if len(tmp) > len(self.longest):
                self.longest = tmp
            a, b, c = sorted(map.items(), key=lambda x: x[1], reverse=True)
            
            if a[1] > 0 and not (len(tmp) >= 2 and tmp[-2::] == a[0]*2):
                map[a[0]] -= 1
                bt(map, tmp+a[0])
                map[a[0]] += 1
            elif b[1] > 0 and not (len(tmp) >= 2 and tmp[-2::] == b[0]*2):
                map[b[0]] -= 1
                bt(map, tmp+b[0])
                map[b[0]] += 1
            elif c[1] >0 and not (len(tmp)>= 2 and tmp[-2::] == c[0]*2):
                map[c[0]] -= 1
                bt(map,tmp+c[0])
                map[c[1]] += 1
        bt(map, '')
        return self.longest
        