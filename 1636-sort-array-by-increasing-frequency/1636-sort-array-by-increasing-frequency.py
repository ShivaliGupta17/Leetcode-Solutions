class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        d={}
        result=[]
        v=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        v=sorted(d.items(),key=lambda x:(x[1],-x[0]) )
        for key,value in v:
            while value:
                result.append(key)
                value-=1
        return result
            


