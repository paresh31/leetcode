class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        alphs=""
        res=""        
        for p in licensePlate:
                if p.isalpha():
                        alphs+=p.lower()
        for word in words:                
                if all(alphs.count(alphs[i]) <= word.count(alphs[i]) for i in range(len(alphs))):
                        if res=="" or len(res)>len(word):
                                res=word
        
        return res