class Solution:
    def addDigits(self, num: int) -> int:
        total=0
        while num>0:
            l=num%10
            num=num//10
            total=l+total
        if total not in [0,1,2,3,4,5,6,7,8,9]:
            return self.addDigits(total)
        else:
            return total

        