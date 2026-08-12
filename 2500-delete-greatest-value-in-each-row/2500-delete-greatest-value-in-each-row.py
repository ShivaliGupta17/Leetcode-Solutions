class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result=0
        for i in range(len(grid)):
            grid[i].sort()
        for i in range(len(grid[0])):
            maxi=float("-inf")
            for row in grid:
               maxi=max(maxi,row[i])
            result+=maxi
        return result


