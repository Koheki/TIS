class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        A,B = 0,0
        countS = collections.defaultdict(int)
        countG = collections.defaultdict(int)
        for s,g in zip(secret,guess):
            if s == g:
                A +=1
            else:
                countS[s]+=1
                countG[g]+=1
        
        for d in [str(i) for i in range(10)]:
            if d in countG and d in countS:
                B += min(countG[d],countS[d])

        return str(A)+'A'+str(B)+'B'
