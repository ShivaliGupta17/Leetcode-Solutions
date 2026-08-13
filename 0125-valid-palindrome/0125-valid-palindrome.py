class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(ch.lower() for ch in s if ch.isalnum())
        left=0
        right=len(s)-1
        for i in range(len(s)):
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True