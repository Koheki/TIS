class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right = 0,sum(nums)
        index = 0

        while index < len(nums):
            right -= nums[index]
            if left == right:
                return index
            left += nums[index]
            index += 1
        return -1
