class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min1=[]
        min1=sorted(arr)
        min_diff=float("inf")
        for i in range(len(min1)-1):
            diff=abs(min1[i]-min1[i+1])
            min_diff=min(min_diff,diff)
        result=[]
        for i in range(len(min1)-1):
            diff=abs(min1[i]-min1[i+1])
            if diff==min_diff:
                result.append([min1[i],min1[i+1]])
        return result
        