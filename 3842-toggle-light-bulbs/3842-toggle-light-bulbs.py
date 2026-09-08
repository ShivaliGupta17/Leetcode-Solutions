class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        #0 pe on and 1 pe off
        d={}
        l=[]
        for bulb in bulbs:
            if bulb in d and d[bulb]==0:
                d[bulb]=1
            else:
                d[bulb]=0
        for bulb in d:
            if d[bulb]==0:    #0 pe off phir on ho jayega agar band bhi hua ho to
                l.append(bulb)
        return sorted(l)



                