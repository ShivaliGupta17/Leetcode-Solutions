class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count=0
        i=0
        for row in mat:
            count=count+row[i]
            i+=1
        j=-1
        for row in mat:
            count=count+row[j]
            j=j-1
        if len(mat)%2!=0:
            row=len(mat)//2
            column=len(mat[0])//2
            count=count-mat[row][column]
        return count