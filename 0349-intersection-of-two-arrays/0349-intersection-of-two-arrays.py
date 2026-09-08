'''class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        if len(nums1)>len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    result.append(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    result.append(nums2[i])
        return list(set(result))'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = set(nums2)
        result = []

        for x in nums1:
            if x in nums2:
                result.append(x)

        return list(set(result))