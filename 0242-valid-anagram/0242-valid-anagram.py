class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        for ch in t:
            d[ch]=d.get(ch,0)-1
        for key,value in d.items():
            if value!=0:
                return False
        return True
        '''
        return sorted(s)==sorted(t)'''

        