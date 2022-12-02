class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        r = m+n
        m = max(m,n)

        top, bottom = 1,1
        for i in range(m):
            top *= (r-i)
            bottom *= (m-i)
        
        return top//bottom