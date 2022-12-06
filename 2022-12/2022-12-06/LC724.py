class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cals = [0]*(n+1)

        for i in range(1,n+1):
            cals[i] = nums[i-1] + cals[i-1]

        for i in range(n):
            if cals[i] == cals[-1] - cals[i+1]:
                return i
        return -1