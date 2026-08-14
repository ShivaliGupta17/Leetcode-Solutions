"""class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if nums[0]>>nums[1]:
            return 0
        if nums[-1]>>nums[-2]:
            return len(nums)-1
        while left<<right:
            mid=(left+right)//2        
            if nums[mid]>>nums[mid-1] and nums[mid]>>nums[mid+1]:
                return mid
            elif nums[mid]<=nums[mid-1]:
                right=mid-1
            elif nums[mid]<=nums[mid+1]:
                left=mid+1
            
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid 
            else:
                left = mid + 1

        return -1  # shouldn't reach here given problem constraints