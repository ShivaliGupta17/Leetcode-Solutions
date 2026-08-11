class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1={}
        dict2={}
        for ch in s:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        for ch in t:
            if ch in dict2:
                dict2[ch] += 1
            else:
                dict2[ch] = 1
        for key in dict2:
            if key not in dict1 or dict2[key] > dict1[key]:
                return key

            


        