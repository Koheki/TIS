nums = [1,100]
l = 0
r = len(nums)-1
nums.sort()
res = set()

while r > l:
    res.add((nums[l]+nums[r])/2)
    l += 1
    r -= 1

print(len(res))