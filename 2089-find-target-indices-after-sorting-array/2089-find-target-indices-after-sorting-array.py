class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        result=[]
        result = sorted(nums)
        l=[]
        for i in range(len(result)):
            if result[i]==target:
                l.append(i)
        return l
