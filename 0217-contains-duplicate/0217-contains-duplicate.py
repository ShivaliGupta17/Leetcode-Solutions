class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''l=[]
        l=sorted(nums)
        if len(nums)==1:
            return False
        for i in range(len(l)-1):
            if l[i]==l[i+1]:
                return True
        else:
            return False'''
        
        return len(set(nums))!=len(nums)

        