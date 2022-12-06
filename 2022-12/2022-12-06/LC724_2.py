class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right = 0,sum(nums)

        pivot = 0
        while pivot < len(nums):
            left += nums[pivot]
            if left == right:
                return pivot
            right -= nums[pivot]
            pivot += 1
        return -1