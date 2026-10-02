class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        d={}
        result=[]
        for i in set(nums1):
            d[i]=d.get(i,0)+1
        for i in set(nums2):
            d[i]=d.get(i,0)+1
        for i in set(nums3):
            d[i]=d.get(i,0)+1
        for key,value in d.items():
            if value>=2:
                result.append(key)
        return result
