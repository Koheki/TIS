# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ok,ng = 0,n+1

        while ng - ok > 1:
            mid = ok + (ng-ok)//2

            if isBadVersion(mid):
                ng = mid
            else:
                ok = mid

        return ng