class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict={}   
        for i in range(len(names)):
            dict.update({heights[i]:names[i]}) 
        ans=[]
        out=[]
        ans=sorted(heights,reverse=True)
        for i in ans:
            out.append(dict[i])
        return out
