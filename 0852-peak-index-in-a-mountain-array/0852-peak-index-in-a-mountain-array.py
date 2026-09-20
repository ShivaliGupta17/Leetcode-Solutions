class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        max=float('-inf')
        left=0
        right=len(arr)-1
        def maxele(left,right):
            mid=(left+right)//2
            if left==right:
                return left
            elif arr[mid]<arr[mid+1]:
                return maxele(mid+1,right)

            else:
                return maxele(left,mid)
        return maxele(left,right)



        