'''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target<=row[-1] and target>=row[0]:
                left=0
                right=len(row)
                while left<=right:

                    mid=left+right//2
                    if row[mid]==target:
                        return True
                    elif row[mid]>=target:
                        right=mid-1
                    else:
                        left=mid+1
        return False
        Line 3: The solution performs a linear scan of the rows, resulting in O(m log n) time complexity.
        it can be solved by making the matrix into single array structure and then perform binary search'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False