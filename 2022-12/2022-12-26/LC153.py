def findMin(nums) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    left,right = 0,n-1

    if nums[right] > nums[0]:
        return nums[0]
    count = 0

    while right >= left or count < 100:
        mid = left + (right-left)//2
        count += 1

        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        
        if nums[mid-1] > nums[mid]:
            return nums[mid]

        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1

nums = list(map(int,input().split()))

print(findMin(nums))