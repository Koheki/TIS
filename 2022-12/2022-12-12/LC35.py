class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = -1,len(nums)

        while r-l > 1:
            m = l + (r-l)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
        return l+1