class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,n):
            nums[i] += nums[i-1]

        for i in range(n):
            left = nums[i-1]
            if i == 0:
                left = 0
            right = nums[n-1] - nums[i]

            if i == n-1:
                right = 0

            if left == right:
                return i

        return -1