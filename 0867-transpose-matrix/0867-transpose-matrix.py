class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        cols=len(matrix[0])
        rows=len(matrix)
        result=[[0] * rows for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                result[j][i]=matrix[i][j]
        return result

        