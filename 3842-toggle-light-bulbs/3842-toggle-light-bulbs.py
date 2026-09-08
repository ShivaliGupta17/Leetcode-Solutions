class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d={}
        l=[]
        for bulb in bulbs:
            if bulb in d and d[bulb]==0:
                d[bulb]=1
            else:
                d[bulb]=0
        for bulb in d:
            if d[bulb]==0:
                l.append(bulb)
        return sorted(l)



                