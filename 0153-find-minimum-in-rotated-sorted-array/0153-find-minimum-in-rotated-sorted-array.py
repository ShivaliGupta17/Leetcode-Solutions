class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        '''total ele=n and digits-0 t0 n-1
        left=0
        right=n-1
        
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[mid-1]:
                right=mid-1
            elif nums[mid]>nums[mid+1]:
                left=mid+1'''
        return min(nums)



        