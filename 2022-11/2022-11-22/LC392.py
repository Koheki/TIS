class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si,ti = 0,0
        ls, lt = len(s),len(t)

        if ls == 0:
            return True

        while ti < lt and si < ls:
            if s[si] == t[ti]:
                si += 1
            if si == ls:
                return True
            ti += 1
        return False
