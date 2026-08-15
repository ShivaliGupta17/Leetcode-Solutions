'''class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = i
            right = len(nums) - 1

            while left < right:
                if nums[left] == nums[right]:
                    return nums[left]
                right -= 1
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        
