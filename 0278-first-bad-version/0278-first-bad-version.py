# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
    
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            n=isBadVersion(mid-1)   
            m =isBadVersion(mid)
            if m is True and n is False:
                return mid          
            elif m is False:
                left = mid + 1
            elif m is True :
                right=mid-1
            
            

               
            
        