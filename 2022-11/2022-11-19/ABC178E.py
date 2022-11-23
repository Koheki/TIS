N = int(input())
d = [[int(n) for n in input().split()] for _ in range(N)]

maxW,minW = -float("inf"), float("inf")
maxZ, minZ = -float("inf"), float("inf")

for i in range(N):
    x,y = d[i]
    w,z = x+y,x-y
    maxW,minW = max(maxW,w),min(minW,w)
    maxZ,minZ = max(maxZ,z),min(minZ,z)

print(max((maxW-minW,maxZ-minZ)))
