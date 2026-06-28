class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        complete = 0

        while n >= row:
            n -= row
            complete += 1
            row += 1

        return complete
        