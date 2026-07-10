class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        result=sorted(nums)
        dis1=0
        count=0
        for i in range(len(result)-1,-1,-1):
            if result[i]!=result[i-1]:
                dis1=result[i]
                count+=1
                if count==3:
                    break
        else :
            return result[-1]
        return dis1      


