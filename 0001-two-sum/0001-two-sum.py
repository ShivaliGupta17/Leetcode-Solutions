class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        dict={}
        for i in range(n):
            remaining=target-nums[i]
            if remaining in dict:
                return [i,dict[remaining]]
            dict[nums[i]]=i