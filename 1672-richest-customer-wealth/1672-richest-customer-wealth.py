class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        '''maxi=0
        for i in range(len(accounts)):
            sums=0
            for j in range(len(accounts[0])):
                sums=sums+accounts[i][j]
            maxi=max(maxi,sums)
        return maxi'''
        maxi=0
        for i in range(len(accounts)):
            sums=sum(accounts[i])
            maxi=max(maxi,sums)
        return maxi

