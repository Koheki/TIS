class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        others = 0
        n = len(nums)

        for zero in range(n):
            if nums[zero] != 0:
                nums[zero],nums[others] = nums[others],nums[zero]
                others += 1

        return