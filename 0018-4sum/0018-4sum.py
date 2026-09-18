class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while left<right:
                    sums=nums[i]+nums[j]+nums[left]+nums[right]
                    if sums==target:
                        result.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-+1
                    elif sums>target:
                        right-=1
                    elif sums<target:
                        left+=1
        return [i for i in result]
