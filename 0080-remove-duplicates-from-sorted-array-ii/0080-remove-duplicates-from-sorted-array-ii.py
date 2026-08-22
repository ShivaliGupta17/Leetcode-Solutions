"""class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        fast=1
        count=0
        while slow<(len(nums)-1):
            
            if nums[slow]==nums[fast] and count==0:
                count+=1
                nums[slow+1]=nums[fast]
                slow+=2
                fast+=1
            elif nums[slow]==nums[fast] and count==1:
                fast+=1
            elif nums[slow]!=nums[fast]:
                fast+=1
        return slow-1"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        count = 1

        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1

        return slow




        