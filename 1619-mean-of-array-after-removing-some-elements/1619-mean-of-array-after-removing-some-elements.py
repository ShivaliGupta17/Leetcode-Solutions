class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        per=int(len(arr)*(5/100))
        total=0
        

        for i in range(per,(len(arr)-per)):
            total=arr[i]+total
        mean=total/(len(arr)-2*per) 
        return mean     