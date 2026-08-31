class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        
        ans = float('inf')
        i, j = 0, len(nums) - 1
        
        while i < j:
            avg = (nums[i] + nums[j]) / 2
            ans = min(ans, avg)
            i += 1
            j -= 1
        
        return ans