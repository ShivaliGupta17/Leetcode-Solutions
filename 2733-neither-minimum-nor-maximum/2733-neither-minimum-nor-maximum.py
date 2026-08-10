class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        '''if len(set(nums))==len(nums) and len(nums)<=2:
            return -1'''
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i+1] and nums[i]!=min(nums) and nums[i]!=max(nums):
                return nums[i]
        else:
            return -1