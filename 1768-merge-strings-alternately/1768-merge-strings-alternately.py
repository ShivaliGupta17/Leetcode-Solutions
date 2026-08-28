'''class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        l1=0
        l2=0
        if len(word1)<len(word2):
            for i in range(len(word1)):
                s=s+word1[l1]
                s=s+word2[l2]
                l1+=1
                l2+=1
                
        else:
            for i in range(len(word2)):
                s=s+word1[l1]
                s=s+word2[l2]
                l1+=1
                l2+=1

        s=s+word1[l1:]
        s=s+word2[l2:]
        return s'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ans.append(word1[i])
            if i < len(word2):
                ans.append(word2[i])

        return ''.join(ans)

        