class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result
        nums = mergeSort(nums)
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        return l
