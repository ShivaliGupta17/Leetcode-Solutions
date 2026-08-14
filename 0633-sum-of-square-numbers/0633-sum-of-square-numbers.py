class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(c**0.5)
        while left<=right:
            b=left**2+right**2
            if b==c:
                return True
            elif c>b:
                left=left+1
            else:
                right=right-1
        return False

        