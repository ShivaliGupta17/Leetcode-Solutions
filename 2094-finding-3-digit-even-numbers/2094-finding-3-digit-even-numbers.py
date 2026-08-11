class Solution:
    def findEvenNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i==j or j==k or k==i:
                        continue
                    if nums[i]==0:
                        continue
                    if nums[k]%2!=0:
                        continue
                    
                    no=nums[i]*100+nums[j]*10+nums[k]
                    result.append(no)
        return sorted(set(result))
            
