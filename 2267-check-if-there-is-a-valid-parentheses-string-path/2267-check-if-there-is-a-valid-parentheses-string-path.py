class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        length = m + n - 1

        # Valid parentheses string ki length even honi chahiye
        if length % 2 == 1:
            return False

        # dp[i][j][balance]
        dp = [
            [
                [False] * (length + 1)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        # Starting cell
        if grid[0][0] == '(':
            dp[0][0][1] = True

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                for balance in range(length + 1):

                    # Current cell '(' hai
                    if grid[i][j] == '(':
                        new_balance = balance + 1

                    # Current cell ')' hai
                    else:
                        new_balance = balance - 1

                    # Invalid balance
                    if new_balance < 0 or new_balance > length:
                        continue

                    # Upar se aa rahe hain
                    if i > 0 and dp[i - 1][j][balance]:
                        dp[i][j][new_balance] = True

                    # Left se aa rahe hain
                    if j > 0 and dp[i][j - 1][balance]:
                        dp[i][j][new_balance] = True

        # End par balance 0 hona chahiye
        return dp[m - 1][n - 1][0]