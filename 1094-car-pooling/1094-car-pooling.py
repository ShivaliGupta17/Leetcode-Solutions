class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        event=[]
        for num,start,end in trips:
            event.append([start,num])
            event.append([end,-num])
        passengers=0
        for location,person in sorted(event):
            passengers+=person
            if passengers>capacity:
                return False
        return True
                

        